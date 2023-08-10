from django.shortcuts import render
from customer.forms import CustomerUploadForm
from customer.models import Customer

# Create your views here.
def upload_customer(request):
    if request.method == "POST":
        form = CustomerUploadForm(request.POST)
        if form.isvalid():
            form.save()
    else:
        form = CustomerUploadForm()
    
    return render(request,"customer/customer_upload.html",{"form":form})

def customer_list(request):
    customers = Customer.objects.all()
    return render(request,"customer/customer_list.html",{"customers": customers})

