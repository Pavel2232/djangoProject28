from django.db import models

# Create your models here.

class Ad(models.Model):
    name= models.CharField(max_length=100)
    author= models.CharField(max_length=200)
    price= models.IntegerField()
    description= models.CharField(max_length=300)
    address= models.CharField(max_length=100)
    is_published= models.BooleanField()

    def __str__(self):
        return self.name