from django.contrib import admin
from task.models import *
# Register your models here.

# @admin.register(ren1,ren2)
class ren1admin(admin.ModelAdmin):
    fieldsets = (
        ('nihao',{'fields':(('title','content'),)}),
        ('basic information',{'fields':['face','laoshi']}),
    )
    pass


class ren2admin(admin.ModelAdmin):
    fieldsets = (
        ('nihao',{'fields':['age']}),
        ('basic information',{'fields':['name']}),
        ('shuru',{'fields':['content']}),
    )

    list_display = ['id','name','age','content',]


admin.site.register(ren1,ren1admin)
admin.site.register(ren2,ren2admin)
admin.site.register(ren3)
admin.site.register(Ren4)