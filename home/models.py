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
