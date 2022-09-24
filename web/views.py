from django.shortcuts import render

def login(request):
    context = {

    }
    return render(request,'web/login.html',context)


def register(request):
    context = {

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
    context = {
        "is_index":True,
    }
    return render(request,'web/index.html',context)


def service(request):
    context = {
        "is_service":True,
    }
    return render(request,'web/service.html',context)


def subService(request):
    context = {
        
    }
    return render(request,'web/sub-services.html',context)


def serviceDetails(request):
    context = {
        
    }
    return render(request,'web/service-details.html',context)


def generatePoster(request):
    context = {
        "is_poster":True,
    }
    return render(request,'web/generate-poster.html',context)


def generateBill(request):
    context = {
        "is_bill":True,
    }
    return render(request,'web/generate-bill.html',context)


def generateForms(request):
    context = {
        "is_form":True,
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
