from turtle import title
from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.db import transaction

from .forms import *
from .models import *
from .generate_frog import generate_fake_frog

# main page
def index(request):
    return render(request, 'frog/index.html')

# adding records
@transaction.atomic
def add(request):
    if request.method == 'POST':
        form = Add_frog_form(request.POST)
        # checking for the correctness of filling in the fields
        if form.is_valid():
            try:
                # if there are less than two honeytoken entries, add
                if Frog.objects.values('honeytoken').filter(honeytoken=True).count() < 2:
                    # generating a random record
                    generate_fake_frog()
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

# getting all the real records
def get(request):
    context = {
        'title' : 'get page', 
        'records' : Frog.objects.get_queryset().filter(honeytoken=False)
        }
    return render(request, 'frog/get.html', context=context)

# deleting by id
def delete(request):
    frog_id = request.GET.get('frog_id')
    try:
        Frog.objects.get(pk=frog_id).delete()
        print(f'frog {frog_id} was deleted')
        return render(request, 'frog/index.html')
    except Frog.DoesNotExist:
        return HttpResponseNotFound("<h2>Frog not found</h2>")    


# errors
# 404
def page_not_found(request, *args, **kvargs):
    print(args, '\n', kvargs)
    return HttpResponseNotFound('<h1>sorry, frogs hid the page....</h1>')

# 500
def server_error(request, *args, **kvargs):
    print(args, '\n', kvargs)
    return HttpResponseNotFound('<h1>sorry, frogs ate the server....</h1>')