from django.db import models

# Create your models here.

class Art(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return self.title


class Mei(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    def __str__(self):
        return self.title

class Mei2(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    content2 = models.TextField(blank=False)
    def __str__(self):
        return self.title

class Mei3(models.Model):
    title = models.CharField(max_length=255)
    laoshi =(
        ("shuxue","dage"),
        ("yingyu","xiaodi"),
        ("yuwen","xiaojie"),
    )
    content = models.TextField(choices=laoshi)

    def __str__(self):
        return self.title

class Mei4(models.Model):
    title = models.CharField(max_length=255)
    laoshi =(
        ("shuxue","dage"),
        ("yingyu","xiaodi"),
        ("yuwen","xiaojie"),
    )
    content = models.CharField(max_length=20,choices=laoshi)
    def __str__(self):
        return self.title


class Mei5(models.Model):
    title = models.CharField(max_length=255)
    laoshi =(
        ("shuxue","dage"),
        ("yingyu","xiaodi"),
        ("yuwen","xiaojie"),
    )
    content = models.CharField(max_length=20,choices=laoshi)
    datatime = models.DateTimeField()
    data = models.DateField()
    def __str__(self):
        return self.title

class Mei6(models.Model):
    title = models.CharField(max_length=255)
    Time = models.TimeField()
    def __str__(self):
        return self.title

class Mei7(models.Model):
    image = models.ImageField()

class Mei8(models.Model):
    image = models.ImageField(upload_to="static/")

class Mei9(models.Model):
    image = models.ImageField(upload_to="/static/",max_length=400)

class Mei10(models.Model):
    image = models.ImageField(upload_to="static/",max_length=400)

class Mei11(models.Model):
    image = models.ImageField(upload_to="static/",width_field=123)

class Mei12(models.Model):
    image = models.FileField(upload_to="static/")

class Mei13(models.Model):
    image = models.FilePathField()

class Mei14(models.Model):
    image = models.GenericIPAddressField()
    def __str__(self):
        return self.image

class Mei15(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return self.name


class Mei16(models.Model):
    name = models.CharField(max_length=100,default='')
    content = models.TextField(default='')
    time = models.TimeField(default="12:00:00")
    fa = models.CharField(choices=(("1","haoren"),("2","huairen"),),default=1,max_length=12)
    def __str__(self):
        return self.name



















