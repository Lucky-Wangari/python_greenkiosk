from django.shortcuts import render
from shipment.forms import ShipmentUploadForm
from shipment.models import Shipment

# Create your views here.
def upload_shipment(request):
    if request.method == "POST":
        form = ShipmentUploadForm(request.POST)
        if form.isvalid():
            form.save()
    else:
        form = ShipmentUploadForm()
    
    return render(request,"shipment/shipment_upload.html",{"form":form})

def shipment_list(request):
    shipments = Shipment.objects.all()
    return render(request,"shipment/shipment_list.html",{"shipments":shipments})
