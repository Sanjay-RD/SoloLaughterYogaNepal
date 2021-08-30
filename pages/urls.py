from django.urls import path
from . import views

urlpatterns=[
    path('/aboutUs',views.aboutus,name="aboutus"),
    path('/gallery',views.gallery,name="gallery"),
    path('/contact',views.contact,name="contact"),
]