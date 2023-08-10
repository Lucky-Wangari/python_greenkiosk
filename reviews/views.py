from django.shortcuts import render
from reviews.admin import ReviewsAdmin
from reviews.forms import ReviewsUploadForm

# Create your views here.
def upload_reviews(request):
    if request.method == "POST":
        form = ReviewsUploadForm(request.POST)
        if form.isvalid():
            form.save()
    else:
        form = ReviewsUploadForm()
    
    return render(request,"reviews/reviews_upload.html",{"form":form})

def review_list(request):
    reviews = ReviewsAdmin.objects.all()
    return render(request,"reviews/reviews_list.html",{"reviews":reviews})
