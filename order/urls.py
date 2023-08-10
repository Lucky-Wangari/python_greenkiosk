from django.urls import path
from order.views import order_list, upload_order


urlpatterns = [
    path("order/upload", upload_order, name="order_upload_view"),
    path("order/list", order_list, name="order_list_view")
    ]