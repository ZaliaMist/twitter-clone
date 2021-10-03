from django.shortcuts import render
from notification.models import Notify
from tweet.models import Tweet
from twitteruser.models import MyUser
from config.settings import AUTH_USER_MODEL


def notification_view(request, notification_id):
    notes = Notify.objects.filter(tagged_user=request.user, is_seen=False)
    notifications = Notify.objects.filter(tagged_user=request.user, is_seen=False)
    for this_notification in notifications:
        this_notification.is_seen = True
        this_notification.save()
    return render(request,
    'notification.html',
    {'notifications': notifications,
    'notes': notes
    })

def allusers_view(request):
    all_users = MyUser.objects.all()
    return render(request, 'allusers.html', {'all_users': all_users})
