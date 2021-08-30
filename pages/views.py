from django.shortcuts import render

# Create your views here.
def aboutus(request):
    return render(request,'pages/aboutus.html')


def gallery(request):
    return render(request,'pages/gallery.html')


def contact(request):
    return render(request,'pages/contact.html')