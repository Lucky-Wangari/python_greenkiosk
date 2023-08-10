from django.urls import path
from .views import product_detail, products_list, upload_product, edit_product_view

urlpatterns = [
    path("products/upload", upload_product, name="product_upload_view"),
    path("products/list", products_list , name ="products_list_view"),
    path("products/<int:id>/", product_detail, name= "product_details_view"),
    path("products/edit/<int:id>/", edit_product_view, name="edit_product_view")
    ]