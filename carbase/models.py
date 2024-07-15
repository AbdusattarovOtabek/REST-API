from django.db import models

from django.contrib.auth.models import User
class Car(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    carname = models.CharField(max_length=200)
    mark = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    mileage = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    img = models.ImageField()
    
    def __str__(self):
        return self.carname
    class Meta:        
        ordering = ['carname']