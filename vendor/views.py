from django.shortcuts import render
from vendor.forms import VendorUploadForm
from vendor.models import Vendor

# Create your views here.
def upload_vendor(request):
    if request.method == "POST":
        form = VendorUploadForm(request.POST)
        if form.isvalid():
            form.save()
    else:
        form = VendorUploadForm()
    
    return render(request,"vendor/vendor_upload.html",{"form":form})

def vendor_list(request):
    vendors = Vendor.objects.all()
    return render(request,"vendor/vendor_list.html",{"vendors":vendors})