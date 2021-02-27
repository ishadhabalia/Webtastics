from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil


def home(request):
    return render(request,'Shop/homepage.html')

def index(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,"Shop/index.html", params)

def about(request):
    return render(request, 'Shop/about.html')

def contact(request):
    return render(request, 'Shop/contact.html')

def tracker(request):
    return render(request, 'Shop/tracker.html')

def search(request):
    return render(request, 'Shop/search.html')

def productView(request,myid):
    #fetch product using id

    product=Product.objects.filter(id = myid)
    return render(request, 'Shop/prodView.html',{'product': product[0]})

def checkout(request):
    return render(request, 'Shop/checkout.html')

