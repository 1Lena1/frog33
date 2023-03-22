from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.http import HttpResponse
from django.shortcuts import render
from .models import Frog


def index(request):
    return render(request, 'frog/index.html')

def add(request):
    return render(request, 'frog/add.html')

def get(request):
    return render(request, 'frog/get.html')


# errors
# 404
def page_not_found(request, *args, **kvargs):
    print(args, '\n', kvargs)
    return HttpResponseNotFound('<h1>sorry, frogs hid the page....</h1>')

# 500
def server_error(request, *args, **kvargs):
    print(args, '\n', kvargs)
    return HttpResponseNotFound('<h1>sorry, frogs ate the server....</h1>')