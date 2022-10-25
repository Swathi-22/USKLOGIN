from notification.models import BroadcastNotification
from web.models import UserRegistration


def notifications(request):
    allnotifications = BroadcastNotification.objects.all()
    return {"notifications": allnotifications}


def profile_image(request):
    user = request.session["phone"]
    logined_user = UserRegistration.objects.get(phone=user)
    return {"logined_user": logined_user, "domain": request.META["HTTP_HOST"]}
