from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def index(request):
    catalogs = Catalog.objects.all()
    news = News.objects.all()
    context = {'catalogs': catalogs, 'news': news}
    return render(request, 'index.html', context)

def contact(request):
    contacts = Contact.objects.get(pk=1)
    context = {'contacts': contacts}
    return render(request, 'contact.html', context)

def view(request, id):
    news = News.objects.all()
    try:
        view = News.objects.get(pk=id)
    except News.DoesNotExist:
        view = None
    context= {'view': view,
              'news': news}
    return render(request, 'view.html', context)
def category(request):
    catalogs = Catalog.objects.all()
    news = News.objects.all()
    context = {'catalogs': catalogs, 'news': news}
    return render(request, 'category.html', context)


