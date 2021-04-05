from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class SkinDiary(models.Model):
    Date= models.DateField()
    Log= models.TextField(max_length=750)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

class HairDiary(models.Model):
    Date= models.DateField()
    Log= models.TextField(max_length=750)
    user= models.ForeignKey(User, on_delete=models.CASCADE)

 

def __str__(self):
    return self.name

