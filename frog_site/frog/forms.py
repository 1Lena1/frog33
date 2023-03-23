import imp
from django import forms
from .models import Frog

class Add_frog_form(forms.Form):
    title = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows':10}))

    