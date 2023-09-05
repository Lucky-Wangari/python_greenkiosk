from django.urls import path
from .views import payment_detail, payment_list, upload_payment


urlpatterns = [
    path("payment/upload", upload_payment, name="payment_upload_view"),
    path("payment/list", payment_list, name="payment_list_view"),
    path("payment/<int:id>/", payment_detail, name= "payment_details_view"),
    ]