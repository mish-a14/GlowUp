from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class SkinDiary(models.Model):
    #Image = models.ImageField(upload_to=get_image_path, blank=True, null=True),
    Date= models.DateField()
    Log= models.TextField(max_length=750)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

class HairDiary(models.Model):
    #Image = models.ImageField(upload_to=get_image_path, blank=True, null=True),
    Date= models.DateField()
    Log= models.TextField(max_length=750)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    #Q) how many days did you track your water intake? 
    #1   2   3   4   5   6   7    

def __str__(self):
    return self.name

#The uploaded image goes to /MEDIA_ROOT/photos/<user_id>/filename
#https://code.google.com/archive/p/django-photologue/
