from django.db import models

# Create your models here.

class image(models.Model):
    iname = models.CharField(max_length=255,default='')
    iurl = models.CharField(max_length=255,default='')
