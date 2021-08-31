from django.shortcuts import render
from .models import Trainer, Schedule

# Create your views here.
def home(request):
    trainers = Trainer.objects.all()
    schedules_one = Schedule.objects.all()[:4]
    schedules_two = Schedule.objects.all()[4:8]
    schedules_three = Schedule.objects.all()[8:12]
    context ={
        'trainers':trainers,
        'schedules_one':schedules_one,
        'schedules_two':schedules_two,
        'schedules_three':schedules_three
    }
    return render(request,'home/index.html',context)
