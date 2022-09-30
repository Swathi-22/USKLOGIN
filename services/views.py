from django.shortcuts import render,get_object_or_404
from services.models import ServiceHeads,Services



def serviceHead(request):
    service_head = ServiceHeads.objects.all()
    context = {
        "is_service":True,
        'service_head':service_head,
    }
    return render(request,'web/service-head.html',context)


def service(request,slug):
    services = Services.objects.filter(service_head__slug=slug)
    context = {
        'services':services,
    }
    return render(request,'web/services.html',context)


def serviceDetails(request,slug):
    services = get_object_or_404(Services,slug=slug)
    context = {
        'services':services,
    }
    return render(request,'web/service-details.html',context)
