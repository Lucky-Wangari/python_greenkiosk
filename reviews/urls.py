from django.urls import path
from .views import review_list, upload_reviews


urlpatterns = [
    path("reviews/upload", upload_reviews, name="reviews_upload_view"),
    path("reviews/list", review_list, name="reviews_list_views"),
    ]