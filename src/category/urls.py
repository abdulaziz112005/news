from django.urls import path

from . import views
app_name='new'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('<int:id>/', views.view, name='info'),
    path('category/', views.category, name='category'),
]