from turtle import title
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import *
from .models import *


def index(request):
    return render(request, 'frog/index.html')

def add(request):
    if request.method == 'POST':
        form = Add_frog_form(request.POST)
        if form.is_valid():
            try:
                Frog.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'error of creating post')
    form = Add_frog_form(request.POST)
    content = {
        'form' : form,
        'title' : 'add page'
    }
    return render(request, 'frog/add.html', content)

def get(request):
    context = {
        'title' : 'get page', 
        'records' : Frog.objects.all()
        }
    return render(request, 'frog/get.html', context=context)

# errors
# 404
def page_not_found(request, *args, **kvargs):
    print(args, '\n', kvargs)
    return HttpResponseNotFound('<h1>sorry, frogs hid the page....</h1>')

# 500
def server_error(request, *args, **kvargs):
    print(args, '\n', kvargs)
    return HttpResponseNotFound('<h1>sorry, frogs ate the server....</h1>')