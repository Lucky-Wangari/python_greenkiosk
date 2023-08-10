from django.contrib import admin
from .models import Reviews
# Register your models here.
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("message","sender","number_of_stars","date")
    
admin.site.register(Reviews,ReviewsAdmin)