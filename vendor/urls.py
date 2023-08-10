from django.urls import path
from .views import  upload_vendor, vendor_list


urlpatterns = [
    path("vendor/upload", upload_vendor, name="upload_vendor_view"),
    path("vendor/list", vendor_list, name="vendor_list_view"),
    ]