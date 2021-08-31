from django.shortcuts import render
from .models import Trainer

# Create your views here.
def home(request):
    trainers = Trainer.objects.all()
    context ={
        'trainers':trainers
    }
    return render(request,'home/index.html',context)
