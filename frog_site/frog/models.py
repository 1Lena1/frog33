from distutils.command.upload import upload
from turtle import title
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Frog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    honeytoken = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    # def __get__(self, *args, **kvargs):
    #     print(f'my honeytoken is {self.honeytoken}')
    #     if self.honeytoken == True:
    #         raise models.Model.DoesNotExist
    #     return self
