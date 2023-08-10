from django.urls import path
from .views import notifications_list, upload_notifications



urlpatterns = [
    path("notifications/upload", upload_notifications, name="notifications_upload_view"),
    path("notifications/list", notifications_list , name ="notifications_list_view"),
]