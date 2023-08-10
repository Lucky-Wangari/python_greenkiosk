from django.urls import path
from .views import payment_list, upload_payment


urlpatterns = [
    path("payment/upload", upload_payment, name="payment_upload_view"),
    path("payment/list", payment_list, name="payment_list_view"),
    ]