from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def index(request):
    catalogs = Catalog.objects.all()
    news = News.objects.all()
    context = {'catalogs': catalogs, 'news': news}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')