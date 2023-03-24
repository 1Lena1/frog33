import imp
from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('add/', add, name='add'),
    path('get/', get, name='get'),
    path('delete/', delete, name='delete'),


]