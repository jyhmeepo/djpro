from django.contrib import admin
from blog.models import *
# Register your models here.


class Arta(admin.ModelAdmin):
    list_display = ['title','content']
class Usera(admin.ModelAdmin):
    list_display = ['username','password']
admin.site.register(User,Usera)
admin.site.register(Art,Arta)

class Quea(admin.ModelAdmin):
    list_display = ['title','content','qt']
admin.site.register(Que,Quea)


admin.site.register(QueT)

admin.site.register(Pro)
admin.site.register(Inv)

admin.site.register(Xm)
admin.site.register(Cy)

admin.site.register(Xs)
admin.site.register(Kp)
admin.site.register(Period)
