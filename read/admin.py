from django.contrib import admin
from read.models import *
# Register your models here.

admin.site.register(Series)
class Perioda(admin.ModelAdmin):
    list_display = ['pname','password']
admin.site.register(Period,Perioda)
admin.site.register(Image)
admin.site.register(Pinfo)
admin.site.register(Tags)