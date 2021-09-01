from django.db import models
from datetime import datetime
from django.db import models
# Create your models here.

class Trainer(models.Model):
    name=models.CharField(max_length=50)
    specified = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profile_image')
    fb_link = models.CharField(max_length=50,blank=True)
    twitter_link = models.CharField(max_length=50,blank=True)
    instagram_link = models.CharField(max_length=50,blank=True)
    is_active = models.BooleanField(default=True)
    joined_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    trainer = models.ForeignKey(Trainer,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    starting_time = models.TimeField()
    ending_time = models.TimeField()
    cover_image = models.ImageField(upload_to="dbImage/schedule")
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title


class Intro(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to="intro")
    is_display = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Advantage(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description = models.TextField(max_length=500,blank=True)
    icon = models.CharField(max_length=50,blank=True)
    is_display = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title