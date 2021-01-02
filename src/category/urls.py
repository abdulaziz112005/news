from django.urls import path

from . import views
app_name = 'new'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact')
]