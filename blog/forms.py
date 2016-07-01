from django import forms
from blog.models import *

class Artf(forms.ModelForm):
    class Meta:
        model = Art
        fields = '__all__'

class Userf(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'