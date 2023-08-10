from django.urls import path
from customer.views import customer_list, upload_customer



urlpatterns = [
    path("customer/upload", upload_customer, name="customer_upload_view"),
    path("customer/list", customer_list , name ="customer_list_view"),]