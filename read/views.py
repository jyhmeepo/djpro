from django.shortcuts import render
from django.http import *
# Create your views here.

def read(req):
    data = {}

    return render(req,'')
    return HttpResponse('read')