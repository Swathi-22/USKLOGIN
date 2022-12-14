import json
import os

from services.models import BrandingImage
from services.models import ServiceHeads
from services.models import Services
from web.constants import PaymentStatus

import razorpay
from .forms import SupportRequestForm
from .forms import SupportTicketForm
from .forms import UserRegistrationForm
from .forms import UserUpdateForm
from .models import FAQ
from .models import AgencyPortal
from .models import AgentBonus
from .models import BackOfficeServices
from .models import CommonServicesPoster
from .models import Documents
from .models import FestivelPoster
from .models import GenerateForms
from .models import ImportantPoster
from .models import LatestNews
from .models import MarketingTips
from .models import NewServicePoster
from .models import Order
from .models import OtherIdeas
from .models import ProfessionalPoster
from .models import Softwares
from .models import Tools
from .models import UserRegistration
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib import messages
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render


def login_view(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        password = request.POST["password"]
        user = UserRegistration.objects.filter(phone=phone).first()
        if user is None:
            print("User Not Found")
            messages.warning(request, "User Not Found")
            return redirect("web:login_view")
        order = Order.objects.get(name=user)
        # obj = UserRegistration.objects.get(phone=phone,password=password)
        profile = UserRegistration.objects.filter(phone=phone, password=password).first()
        if profile is None:
            messages.warning(request, "Wrong Password")
            return redirect("web:login_view")

        if user is not None and order.status == PaymentStatus.SUCCESS:
            request.session["phone"] = user.phone
            # messages.success(request, "You have successfully logged in!")
            return redirect("web:index")

        if order.status == PaymentStatus.FAILURE or order.status == PaymentStatus.PENDING:
            messages.info(request, "Please complete your payment")
            return redirect("web:login_view")

        # is_user = UserRegistration.objects.filter(is_user=True)
        # print(is_user)

        # if user is not None and order.status == PaymentStatus.SUCCESS:
        #     # if user is not None and is_user:
        #     request.session['phone'] = phone
        #     request.session['password'] = password
        #     messages.success(request, 'You have successfully logged in!', 'success')
        #     return redirect('web:index')
        # elif order.status == PaymentStatus.FAILURE or order.status == PaymentStatus.PENDING:
        #     messages.info(request, 'Please complete your payment')
        # else:
        #     messages.info(request, 'Invalid username or password')
        #     return redirect('web:login_view')
    return render(request, "web/login.html")


# @csrf_exempt
def register(request):
    user_form = UserRegistrationForm(request.POST or None)
    context = {"user_form": user_form}
    return render(request, "web/register.html", context)


def order_payment(request):
    user_form = UserRegistrationForm(request.POST or None)
    if request.method == "POST":
        email = request.POST.get("email")
        amount = 20000
        if user_form.is_valid():
            user_form.save()
        client = razorpay.Client(auth=("rzp_test_kVa6uUqaP96eJr", "SMxZvHU0XyiAIwMoLIqFL7Na"))
        razorpay_order = client.order.create({"amount": amount, "currency": "INR", "payment_capture": "1"})
        obj = UserRegistration.objects.get(email=email)
        order = Order.objects.create(name=obj, amount=amount, provider_order_id=razorpay_order["id"])
        order.save()

        return render(
            request,
            "web/payment.html",
            {
                # "callback_url": "https://" + "usklogin.geany.website" + "/callback/",
                "callback_url": "http://" + "127.0.0.1:7000" + "/callback/",
                "razorpay_key": "rzp_test_kVa6uUqaP96eJr",
                "order": order,
            },
        )
    return render(request, "web/payment.html")


# @csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=("rzp_test_kVa6uUqaP96eJr", "SMxZvHU0XyiAIwMoLIqFL7Na"))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")

        order = Order.objects.get(provider_order_id=provider_order_id)

        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if not verify_signature(request.POST):
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "web/callback.html", context={"status": order.status})
        else:
            order.status = PaymentStatus.SUCCESS
            order.save()
            return render(request, "web/callback.html", context={"status": order.status})
    else:
        return render(request, "web/payment.html")


def forgot_password(request):
    context = {}
    return render(request, "web/forgot-password.html", context)


def profile(request):
    user = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=user)
    user_form = UserUpdateForm(request.POST, request.FILES, instance=logined_user)
    context = {"is_profile": True, "logined_user": logined_user, "user_form": user_form}
    return render(request, "web/profile.html", context)


def profile_update(request):
    user = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=user)
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, request.FILES, instance=logined_user)
        if user_form.is_valid():
            user_form.save()
            return redirect("web:profile")
    else:
        user_form = UserUpdateForm(instance=logined_user)
    context = {"user_form": user_form}
    return render(request, "web/profile-update.html", context)


def settings(request):
    context = {}
    return render(request, "web/settings.html", context)


def index(request):
    service_head = ServiceHeads.objects.all()
    latest_news = LatestNews.objects.all().last()
    new_service_poster = NewServicePoster.objects.all()
    important_poster = ImportantPoster.objects.all()
    # user = UserRegistration.objects.filter(phone=phone).last()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {
        "is_index": True,
        "service_head": service_head,
        "latest_news": latest_news,
        "new_service_poster": new_service_poster,
        "important_poster": important_poster,
        "room_name": "broadcast",
        "logined_user": logined_user,
    }
    return render(request, "web/index.html", context)


def notes(request):
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"logined_user": logined_user}
    return render(request, "web/notes.html", context)


def notification(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("notification_broadcast", {"type": "send_notification", "message": "Notification"})
    return HttpResponse("Done")


def generatePoster(request):
    common_services_poster = CommonServicesPoster.objects.all()
    festivel_poster = FestivelPoster.objects.all()
    professional_poster = ProfessionalPoster.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    branding_image = BrandingImage.objects.all()

    context = {
        "is_poster": True,
        "common_services_poster": common_services_poster,
        "festivel_poster": festivel_poster,
        "professional_poster": professional_poster,
        "logined_user": logined_user,
        "branding_image": branding_image,
    }
    return render(request, "web/generate-poster.html", context)


def generateBill(request):
    services = Services.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"is_bill": True, "services": services, "logined_user": logined_user}
    return render(request, "web/generate-bill.html", context)


def searchResult(request):
    if request.is_ajax():
        res = None
        services = request.POST.get("services")
        service_search = Services.objects.filter(title__icontains=services)
        if len(service_search) > 0 and len(services) > 0:
            data = []
            for i in service_search:
                items = {"pk": i.pk, "name": i.title}
                data.append(items)
            res = data
        else:
            res = "No sevice found"
        return JsonResponse({"data": res})
    return JsonResponse({})


def invoice(request):
    context = {"is_bill": True}
    return render(request, "web/invoices.html", context)


def generateForms(request):
    generate_forms = GenerateForms.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"is_form": True, "generate_forms": generate_forms, "logined_user": logined_user}
    return render(request, "web/generate-form.html", context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, "rb") as fh:
            response = HttpResponse(fh.read(), content_type="application/file")
            response["Content-Disposition"] = "inline;filename=" + os.path.basename(file_path)
            return response
    raise Http404


def documents(request):
    documents = Documents.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"is_document": True, "documents": documents, "logined_user": logined_user}
    return render(request, "web/documents.html", context)


def software(request):
    softwares = Softwares.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"is_software": True, "softwares": softwares, "logined_user": logined_user}
    return render(request, "web/softwares.html", context)


def tools(request):
    tools = Tools.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"is_tool": True, "tools": tools, "logined_user": logined_user}
    return render(request, "web/tools.html", context)


def marketingTip(request):
    marketing_tips = MarketingTips.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"is_tip": True, "marketing_tips": marketing_tips, "logined_user": logined_user}
    return render(request, "web/marketing-tip.html", context)


def otherIdea(request):
    other_ideas = OtherIdeas.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"is_idea": True, "other_ideas": other_ideas, "logined_user": logined_user}
    return render(request, "web/other-ideas.html", context)


def agencyPortal(request):
    agency_portal = AgencyPortal.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"is_portal": True, "agency_portal": agency_portal, "logined_user": logined_user}
    return render(request, "web/agency-portal.html", context)


def backOfficeServices(request):
    back_office_services = BackOfficeServices.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"is_backservice": True, "back_office_services": back_office_services, "logined_user": logined_user}
    return render(request, "web/back-office-services.html", context)


def bonus(request):
    agent_bonus = AgentBonus.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"is_bonus": True, "agent_bonus": agent_bonus, "logined_user": logined_user}
    return render(request, "web/bonus.html", context)


def support(request):
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"is_support": True, "logined_user": logined_user}
    return render(request, "web/support.html", context)


def supportRequest(request):
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    forms = SupportRequestForm(request.POST or None)
    if request.method == "POST":
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {"status": "true", "title": "Successfully Submitted", "message": "Message successfully submitted"}
        else:
            response_data = {"status": "false", "title": "Form validation error", "message": repr(forms.errors)}
        return HttpResponse(json.dumps(response_data), content_type="application/javascript")
    context = {"forms": forms, "logined_user": logined_user}
    return render(request, "web/support-request.html", context)


def F_A_Q(request):
    Frequently_Asked_Questions = FAQ.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"Frequently_Asked_Questions": Frequently_Asked_Questions, "logined_user": logined_user}
    return render(request, "web/faq.html", context)


def supportTicket(request):
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    forms = SupportTicketForm(request.POST or None)
    if request.method == "POST":
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {"status": "true", "title": "Successfully Submitted", "message": "Message successfully submitted"}
        else:
            response_data = {"status": "false", "title": "Form validation error", "message": repr(forms.errors)}
        return HttpResponse(json.dumps(response_data), content_type="application/javascript")
    context = {"forms": forms, "logined_user": logined_user}
    return render(request, "web/support-ticket.html", context)


def termsConditions(request):
    context = {}
    return render(request, "web/terms&conditions.html", context)


def payment(request):
    context = {}
    return render(request, "web/payment.html", context)


def paymentsuccess(request):
    context = {}
    return render(request, "web/paymentsuccess.html", context)


def paymentfail(request):
    context = {}
    return render(request, "web/paymentfail.html", context)


def logout(request):
    del request.session["phone"]
    return redirect("web:login")
