from . import views
from django.urls import path

urlpatterns = [
    
    path("", views.home, name = 'Home'),
    path("shop/", views.index, name = 'ShopHome'),
    path("about/", views.about, name = 'AboutUs'),
    path("contact/", views.contact, name = 'ContactUs'),
    path("shop/tracker/", views.tracker, name = 'TrackingStatus'),
    path("shop/search/", views.search, name = 'Search'),
    path("shop/products/<int:myid>", views.productView, name = 'ProductView'),
    path("shop/checkout", views.checkout, name = 'Checkout')
    
]