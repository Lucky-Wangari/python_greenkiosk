from django.shortcuts import redirect, render
from cart.forms import CartUploadForm
from cart.models import Cart

# Create your views here.
def upload_cart(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = CartUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CartUploadForm()
    return render(request, "cart/cart_upload.html", {"form": form})

def cart_list(request):
    carts = Cart.objects.all()
    return render(request,"cart/cart_list.html",{"carts":carts})

def cart_detail(request,id):
    carts = Cart.objects.get(id = id)
    return render(request,"inventory/product_detail.html",{"carts":carts})

def edit_cart_view(request, id):
    cart = Cart.objects.get(id=id)
    if request.method == "POST":
        form = CartUploadForm(request.POST, instance= cart)
        if form.valid():
            form.save()
        return redirect("cart_detail_view", id)

    else: 
        form = CartUploadForm(instance= cart)
        return render(request, "cart/edit_cart.html", {"form": form})


















