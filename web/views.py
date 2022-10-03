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



@csrf_exempt
def login(request):
    context = {

    }
    return render(request,'web/login.html',context)


@csrf_exempt
def register(request):
    user_form = UserRegistrationForm(request.POST or None)
    print(user_form)
    if request.method == "POST":
        if user_form.is_valid():
            user_form.save()
            return redirect('web:order_payment')
    context = {
        'user_form':user_form
    }
    return render(request,'web/register.html',context)


def forgot_password(request):
    context = {

    }
    return render(request,'web/forgot-password.html',context)


def profile(request):
    context = {
        "is_profile":True,
    }
    return render(request,'web/profile.html',context)


def settings(request):
    context = {

    }
    return render(request,'web/settings.html',context)


def index(request):
    service_head = ServiceHeads.objects.all()
    latest_news = LatestNews.objects.all().last()
    new_service_poster = NewServicePoster.objects.all()
    important_poster = ImportantPoster.objects.all()
    context = {
        "is_index":True,
        'service_head':service_head,
        'latest_news':latest_news,
        'new_service_poster':new_service_poster,
        'important_poster':important_poster,
    }
    return render(request,'web/index.html',context)


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



def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type = 'application/file')
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404


def generateBill(request):
    context = {
        "is_bill":True,
    }
    return render(request,'web/generate-bill.html',context)


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




def documents(request):
    context = {
        "is_document":True,
    }
    return render(request,'web/documents.html',context)


def software(request):
    context = {
        "is_software":True,
    }
    return render(request,'web/softwares.html',context)


def tools(request):
    context = {
        "is_tool":True,
    }
    return render(request,'web/tools.html',context)


def marketingTip(request):
    context = {
        "is_tip":True,
    }
    return render(request,'web/marketing-tip.html',context)


def otherIdea(request):
    context = {
        "is_idea":True,
    }
    return render(request,'web/other-ideas.html',context)


def agencyPortal(request):
    context = {
        "is_portal":True,
    }
    return render(request,'web/agency-portal.html',context)


def backOfficeServices(request):
    context = {
        "is_backservice":True,
    }
    return render(request,'web/back-office-services.html',context)


def bonus(request):
    context = {
        "is_bonus":True,
    }
    return render(request,'web/bonus.html',context)


def support(request):
    context = {
        "is_support":True,
    }
    return render(request,'web/support.html',context)


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




# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(auth=("rzp_test_gK01XfmKtlAa9L", "afRPwwosjKxVWtD2UGyhHyVD"))
 
 
def order_payment(request):
    currency = 'INR'
    amount = 20000  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = '/paymentsuccess/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = "rzp_test_gK01XfmKtlAa9L"
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'web/payment.html', context=context)
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'web/paymentsuccess.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'web/paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'web/paymentsuccess.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()






