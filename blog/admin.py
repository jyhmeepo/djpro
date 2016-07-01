from django.contrib import admin
from blog.models import *
# Register your models here.


class Arta(admin.ModelAdmin):
    list_display = ['title','content']
class Usera(admin.ModelAdmin):
    list_display = ['username','password']
admin.site.register(User,Usera)
admin.site.register(Art,Arta)
