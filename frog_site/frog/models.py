from distutils.command.upload import upload
from turtle import title
from django.db import models

# Create your models here.
class Frog(models.Model):
    title = models.CharField(max_length=255)
    contet = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

