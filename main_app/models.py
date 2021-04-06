from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class SkinDiary(models.Model):
    Date= models.DateField()
    Log= models.TextField(max_length=750)
    Water = models.BooleanField()
    Product = models.TextField(max_length=100)
    Morning = models.BooleanField()
    Night = models.BooleanField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Log

class HairDiary(models.Model):
    Date= models.DateField()
    Log= models.TextField(max_length=750)
    Water = models.BooleanField()
    Product = models.TextField(max_length=100)
    Morning = models.BooleanField()
    Night = models.BooleanField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Log


#need to add images into the models 
class Hair_Photo(models.Model):
    url = models.CharField(max_length=300)
    hair = models.ForeignKey(HairDiary, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"Photo for hair_id: {self.hair_id} @{self.url}"

class Skin_Photo(models.Model):
    url = models.CharField(max_length=300)
    skin = models.ForeignKey(SkinDiary, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"Photo for skin_id: {self.skin_id} @{self.url}"

