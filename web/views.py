from multiprocessing import context
from pyexpat.errors import messages
from urllib import response
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import *
import razorpay
from django.http import Http404, HttpResponseBadRequest,HttpResponse
from services.models import *
from web.models import *
import mimetypes
import os
import json
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync



def login_view(request):

    # login_form = LoginForm(request.POST or None)
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        user = UserRegistration.objects.filter(phone=phone,password=password)
        if user is not None:
            request.session['phone'] = phone
            messages.success(request, 'You have successfully logged in!', 'success')
            return redirect('web:index')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('web:login_view')
    return render(request,'web/login.html')


@csrf_exempt
def register(request):
    user_form = UserRegistrationForm(request.POST or None)
    context = {
        'user_form':user_form
    }
    return render(request,'web/register.html',context)



def order_payment(request):
    user_form = UserRegistrationForm(request.POST or None)
    if request.method == "POST":
        email = request.POST.get("email")
        amount = 20000
        if user_form.is_valid():
            user_form.save()
        client = razorpay.Client(auth=("rzp_test_hC4pFTo1gvL3SV", "lYvTTabO6PRGJMTwV6JPgEa5"))
        razorpay_order = client.order.create({"amount":amount , "currency": "INR", "payment_capture": "1"})
        obj = UserRegistration.objects.get(email=email)
        order = Order.objects.create(name=obj, amount=amount, provider_order_id=razorpay_order["id"])
        order.save()

        return render(
            request,
            "web/payment.html",
            {
                # "callback_url": "https://" + "razorpaytask.herokuapp.com" + "/callback/",
                "callback_url": "http://" + "127.0.0.1:8000" + "/callback/",
                "razorpay_key": 'rzp_test_hC4pFTo1gvL3SV',
                "order": order,
            },
        )
    return render(request,"web/payment.html")


@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=("rzp_test_hC4pFTo1gvL3SV", "lYvTTabO6PRGJMTwV6JPgEa5"))
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
    context = {

    }
    return render(request,'web/forgot-password.html',context)


def profile(request):
    user=request.session['phone']
    logined_user=UserRegistration.objects.get(phone=user)
    context = {
        "is_profile":True,
        'logined_user':logined_user
    }
    return render(request,'web/profile.html',context)



def profile_update(request):
    # if request.method == 'POST':
    #     user_form = UserUpdateForm(request.POST,request.FILES,instance=request.session['phone'])
    # else:
    #     user_form = UserUpdateForm(instance=request.session['phone'])
    context = {
        # 'user_form':user_form
    }
    return render(request,'web/profile-update.html',context)


def settings(request):
    context = {

    }
    return render(request,'web/settings.html',context)


def index(request):
    service_head = ServiceHeads.objects.all()[:12]
    latest_news = LatestNews.objects.all().last()
    new_service_poster = NewServicePoster.objects.all()
    important_poster = ImportantPoster.objects.all()
    user=request.session['phone']
    logined_user=UserRegistration.objects.get(phone=user)
    context = {
        "is_index":True,
        'service_head':service_head,
        'latest_news':latest_news,
        'new_service_poster':new_service_poster,
        'important_poster':important_poster,
        'room_name':"broadcast",
        'logined_user':logined_user
    }
    return render(request,'web/index.html',context)



def notification(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type':'send_notification',
            'message':"Notification"
        }
    )
    return HttpResponse("Done")



def generatePoster(request):
    common_services_poster = CommonServicesPoster.objects.all()
    festivel_poster = FestivelPoster.objects.all()
    professional_poster = ProfessionalPoster.objects.all()
    context = {
        "is_poster":True,
        'common_services_poster':common_services_poster,
        'festivel_poster':festivel_poster,
        'professional_poster':professional_poster,
    }
    return render(request,'web/generate-poster.html',context)



def generateBill(request):
    services=Services.objects.all()   
    context = {
        "is_bill":True,
        'services':services,
    }
    return render(request,'web/generate-bill.html',context)


def searchResult(request):
    if request.is_ajax():
        res = None
        services = request.POST.get('services')
        service_search = Services.objects.filter(title__icontains=services)
        if len(service_search) > 0 and len(services) > 0:
            data = []
            for i in service_search:
                items = {
                    'pk':i.pk,
                    'name':i.title
                }
                data.append(items)
            res = data
        else:
            res = 'No sevice found'
        return JsonResponse({'data':res})
    return JsonResponse({})



def invoice(request):
    context = {
        "is_bill":True,
    }
    return render(request,'web/invoices.html',context)


def generateForms(request):
    generate_forms = GenerateForms.objects.all()
    context = {
        "is_form":True,
        'generate_forms':generate_forms
    }
    return render(request,'web/generate-form.html',context)


def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type = 'application/file')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404



def documents(request):
    documents = Documents.objects.all()
    context = {
        "is_document":True,
        'documents':documents,
    }
    return render(request,'web/documents.html',context)


def software(request):
    softwares = Softwares.objects.all()
    context = {
        "is_software":True,
        'softwares':softwares,
    }
    return render(request,'web/softwares.html',context)


def tools(request):
    tools=Tools.objects.all()
    context = {
        "is_tool":True,
        'tools':tools,
    }
    return render(request,'web/tools.html',context)


def marketingTip(request):
    marketing_tips = MarketingTips.objects.all()
    context = {
        "is_tip":True,
        'marketing_tips':marketing_tips,
    }
    return render(request,'web/marketing-tip.html',context)


def otherIdea(request):
    other_ideas=OtherIdeas.objects.all()
    context = {
        "is_idea":True,
        'other_ideas':other_ideas,
    }
    return render(request,'web/other-ideas.html',context)


def agencyPortal(request):
    agency_portal = AgencyPortal.objects.all()
    context = {
        "is_portal":True,
        'agency_portal':agency_portal,
    }
    return render(request,'web/agency-portal.html',context)


def backOfficeServices(request):
    back_office_services=BackOfficeServices.objects.all()
    context = {
        "is_backservice":True,
        'back_office_services':back_office_services,
    }
    return render(request,'web/back-office-services.html',context)


def bonus(request):
    agent_bonus = AgentBonus.objects.all()
    context = {
        "is_bonus":True,
        'agent_bonus':agent_bonus,
    }
    return render(request,'web/bonus.html',context)


def support(request):
    context = {
        "is_support":True,
    }
    return render(request,'web/support.html',context)


def supportRequest(request):
    forms = SupportRequestForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully submitted"
            }
        else:
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": repr(forms.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    context={
        'forms':forms
    }
    return render(request,'web/support-request.html',context)


def F_A_Q(request):
    Frequently_Asked_Questions= FAQ.objects.all()
    context = {
        'Frequently_Asked_Questions':Frequently_Asked_Questions,
    }
    return render(request,'web/faq.html',context)


def supportTicket(request):
    forms = SupportTicketForm(request.POST or None)
    if request.method == 'POST':
        if forms.is_valid():
            data = forms.save(commit=False)
            data.referral = "web"
            data.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully submitted"
            }
        else:
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": repr(forms.errors)
            }
        return HttpResponse(json.dumps(response_data), content_type='application/javascript')
    context={
        'forms':forms
    }
    return render(request,'web/support-ticket.html',context)


def termsConditions(request):
    context = {
        
    }
    return render(request,'web/terms&conditions.html',context)


def payment(request):
    context = {
        
    }
    return render(request,'web/payment.html',context)


def paymentsuccess(request):
    context = {
        
    }
    return render(request,'web/paymentsuccess.html',context)


def paymentfail(request):
    context = {
        
    }
    return render(request,'web/paymentfail.html',context)


def logout(request):
    try:
        del request.session['phone']
    except:
        return redirect('web:login_view')
    return redirect('web:login_view')
    





