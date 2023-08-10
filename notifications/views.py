from django.shortcuts import render
from notifications.forms import NotificationsUploadForm
from notifications.models import Notifications

# Create your views here.
def upload_notifications(request):
    if request.method == "POST":
        form = NotificationsUploadForm(request.POST)
        if form.isvalid():
            form.save()
    else:
        form = NotificationsUploadForm()
    
    return render(request,"customer/customer_upload.html",{"form":form})

def notifications_list(request):
    notifications = Notifications.objects.all()
    return render(request,"notifications/notifications_list.html",{"notifications":notifications})



