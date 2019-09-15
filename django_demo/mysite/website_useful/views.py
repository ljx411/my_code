from django.shortcuts import render
from website_useful.models import Category, UrlTools


# Create your views here.

def get_Category(request):
    return render(request, "website_useful/category.html")
