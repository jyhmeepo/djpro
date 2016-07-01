from django import forms
from task.models import *


class renf1(forms.ModelForm):
    class Meta:
        model = ren1
        fields = ['title','content','laoshi','face']


class Ren4f(forms.ModelForm):
    class Meta:
        model = Ren4
        fields ='__all__'

class Ren4f2(forms.Form):

    pass


class F1(forms.Form):
    name = forms.CharField(label='name(选填)',max_length=2,widget=forms.Textarea(attrs={'class': 'form-control'}))
    age = forms.IntegerField(max_value=1,widget=forms.TextInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    url = forms.URLField(widget=forms.TextInput(attrs={'class': 'form-control'}))