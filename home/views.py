from django.shortcuts import render
from .models import Trainer, Schedule, Intro, Advantage

# Create your views here.
def home(request):
    trainers = Trainer.objects.all()
    schedules_one = Schedule.objects.all()[:4]
    schedules_two = Schedule.objects.all()[4:8]
    schedules_three = Schedule.objects.all()[8:12]
    intros = Intro.objects.all()[:1]
    advantages_left = Advantage.objects.all()[:3]
    advantages_right = Advantage.objects.all()[3:6]
    context ={
        'trainers':trainers,
        'schedules_one':schedules_one,
        'schedules_two':schedules_two,
        'schedules_three':schedules_three,
        'intros':intros,
        'advantages_left':advantages_left,
        'advantages_right':advantages_right
    }
    return render(request,'home/index.html',context)
