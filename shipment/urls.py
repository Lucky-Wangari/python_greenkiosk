from django.urls import path
from .views import shipment_list, upload_shipment


urlpatterns = [
    path("shipment/upload", upload_shipment, name="shipment_upload_view"),
    path("shipment/list", shipment_list, name="shipment_list_view"),
    ]