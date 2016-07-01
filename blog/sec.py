from django.views.generic import *
from blog.models import *
class About(ListView):
    model = User
    context_object_name = "artll"