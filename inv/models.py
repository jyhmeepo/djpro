from django.db import models

# Create your models here.

class Comp(models.Model):
    name = models.CharField(max_length=255,default='',blank=True)
    money = models.CharField(max_length=255,default='',blank=True)
    def __str__(self):
        return self.name
