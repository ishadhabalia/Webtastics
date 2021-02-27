from django.shortcuts import render
from .models import Product, Contact, Orders
from math import ceil
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
from django.http import HttpResponse


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
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'Shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'Shop/checkout.html')

