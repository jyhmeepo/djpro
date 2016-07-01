from django import forms
from news.models import *

class Name(forms.Form):
    name = forms.CharField(label='name',max_length=100)
    content = forms.CharField(label='content',max_length=100)
    # text = forms.Textarea()
    # cc = (
    #     ('l','yuwen'),
    #     ('m','shuxue'),
    #     ('n','yingyu'),
    # )
    # love = forms.ChoiceField(choices=cc)

class mform(forms.ModelForm):
    class Meta:
        model = Mei16
        fields =['name','content','time','fa',]


