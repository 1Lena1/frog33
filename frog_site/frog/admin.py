from django.contrib import admin

from .models import *

class Frog_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'honeytoken')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


# registration of the frog class admin
admin.site.register(Frog, Frog_admin)
