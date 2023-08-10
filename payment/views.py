from django.shortcuts import render
from payment.forms import PaymentUploadForm
from payment.models import Payment

# Create your views here.
def upload_payment(request):
    if request.method == "POST":
        form = PaymentUploadForm(request.POST)
        if form.isvalid():
            form.save()
    else:
        form = PaymentUploadForm()
    
    return render(request,"payment/payment_upload.html",{"form":form})


def payment_list(request):
    payments = Payment.objects.all()
    return render(request,"payment/payment_list.html",{"payments":payments})


