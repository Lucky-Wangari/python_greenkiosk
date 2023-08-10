from django.urls import path
from cart.views import cart_detail, cart_list, edit_cart_view, upload_cart

urlpatterns = [
    path("cart/upload", upload_cart, name="cart_upload_view"),
    path("cart/list", cart_list, name= "cart_list_view"),
    path("cart/<int:id>/", cart_detail, name= "cart_details_view"),
    path("cart/edit/<int:id>/", edit_cart_view, name="edit_cart_view")
    ]