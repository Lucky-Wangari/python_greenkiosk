from django.shortcuts import render
from order.forms import OrderUploadForm
from order.models import Order

# Create your views here.
def upload_order(request):
    if request.method == "POST":
        form = OrderUploadForm(request.POST)
        if form.isvalid():
            form.save()
    else:
        form = OrderUploadForm()
    
    return render(request,"order/order_upload.html",{"form":form})

def order_list(request):
    orders = Order.objects.all()
    return render(request,"order/order_list.html",{"orders":orders})

