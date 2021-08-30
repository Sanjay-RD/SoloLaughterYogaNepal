from django.shortcuts import render

# Create your views here.

def booking(request):
    return render(request,'schedule/booking.html')


def appointment(request):
    return render(request,'schedule/appointment.html')

