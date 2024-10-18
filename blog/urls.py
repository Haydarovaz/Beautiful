from django.urls import path

from .views import index,about,base,client,contact,index,products

urlpatterns = [
    path('', index, name = 'index'),
    path('about', about, name = 'about'),
    path('base', base, name = 'base'),
    path('client', client, name = 'client'),
    path('contact', contact, name = 'contact'),
    path('index', index, name = 'index'),
    path('products', products, name = 'products')
 ]