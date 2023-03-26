from distutils.command.upload import upload
from tabnanny import verbose
from turtle import title
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

# frog to see: Frog.objects.filter(honeytoken=False)
class Frog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    honeytoken = models.BooleanField(default=False)
    

    def __str__(self) -> str:
        return self.title

    