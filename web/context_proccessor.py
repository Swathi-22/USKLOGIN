from notification.models import BroadcastNotification


def notifications(request):
    allnotifications = BroadcastNotification.objects.all()
    return {"notifications": allnotifications}


def profile_image(request):
    phone=request.session['phone']
    logined_user = UserRegistration.objects.filter(phone=phone).first()
    return {
        'logined_user':logined_user,
        'domain':request.META['HTTP_HOST']
    }

