from django import forms
from .models import Reviews

class ReviewsUploadForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = "__all__"