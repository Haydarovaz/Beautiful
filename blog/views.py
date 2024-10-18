from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', context={})

def about(request):
    return render(request, 'about.html', context={})
def base(request):
    return render(request, 'base.html', context={})
def client(request):
    return render(request, 'client.html', context={})
def contact(request):
    return render(request, 'contact.html', context={})
def index(request):
    return render(request, 'index.html', context={})
def products(request):
    return render(request, 'products.html', context={})
