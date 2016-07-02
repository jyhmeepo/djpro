from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=255,default='')
    password = models.CharField(max_length=255,default='')
    createtime =models.DateTimeField()
    def __str__(self):
        return self.username

class Art(models.Model):
    title = models.CharField(max_length=255,default='')
    content = models.TextField(default='')
    def __str__(self):
        return self.title


class QueT(models.Model):
    tt = models.CharField(max_length=255,default='')
    tt2 = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.tt

class Que(models.Model):
    title = models.CharField(max_length=255,default='')
    content = models.CharField(max_length=255,default='')
    qt = models.ForeignKey(QueT)
    def __str__(self):
        return self.title


class Pro(models.Model):
    pname = models.CharField(max_length=255, default='')
    total = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.pname

class Inv(models.Model):
    iname = models.CharField("inv name",max_length=255,default='')
    money = models.IntegerField(default=0)
    project = models.ForeignKey(Pro)
    project2 = models.CharField(max_length=255,default='',choices={("xm1","shiyou"),("xm2","dianxin")})
    def __str__(self):
        return self.iname


class Xm(models.Model):
    xname = models.CharField(max_length=255,default='')
    value = models.IntegerField(default=0)
    def __str__(self):
        return self.xname

class Cy(models.Model):
    cname = models.CharField(max_length=255, default='')
    old = models.IntegerField(default=0)
    xm = models.ManyToManyField(Xm)
    def __str__(self):
        return self.cname


class Kp(models.Model):
    kname = models.CharField(max_length=255, default='')
    def __str__(self):
        return self.kname

class Xs(models.Model):
    xname = models.CharField(max_length=255, default='')
    xm = models.OneToOneField(Kp)
    def full(self):
        return self.xname+'kkk'
    def __str__(self):
        return self.xname


class Base(models.Model):
    createtime = models.IntegerField(default=0)

class Series(Base):
    name = models.CharField(max_length=255,default='')


class Period(models.Model):
    name = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.name