from services.models import ServiceHeads
from services.models import Services
from web.models import UserRegistration

from django.shortcuts import get_object_or_404
from django.shortcuts import render


def serviceHead(request):
    service_head = ServiceHeads.objects.all()
    services = Services.objects.all()
    phone = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=phone)
    context = {"is_service": True, "service_head": service_head, "services": services, "logined_user": logined_user}
    return render(request, "web/service-head.html", context)


# def service(request,slug):
#     services = Services.objects.filter(service_head__slug=slug)
#     context = {
#         'services':services,
#     }
#     return render(request,'web/services.html',context)


def serviceDetails(request, slug):
    services = get_object_or_404(Services, slug=slug)
    print(services.video_tutorial)
    context = {"services": services}
    return render(request, "web/service-details.html", context)
