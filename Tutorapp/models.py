from django.db import models

class Client(models.Model):
    Name=models.CharField(max_length=30)
    slug=models.SlugField(max_length=150,verbose_name="Student Slug",null=True)
    Email=models.EmailField()
    Standard=models.CharField(max_length=15)
    Phone=models.IntegerField()
    Password=models.CharField(max_length=15)
    ConPassword=models.CharField(max_length=15)

class Tutor(models.Model):
    Name=models.CharField(max_length=30,verbose_name="Name")
    slug=models.SlugField(max_length=150,verbose_name="Tutor slug",null=True)
    category_image = models.ImageField(upload_to='Tutor', blank=True, null=True, verbose_name="Image")
    Subject=models.CharField(max_length=100,verbose_name="Subject")
    Qualification=models.CharField(max_length=30,verbose_name="Qualification")
    Experience=models.IntegerField(verbose_name="Experience")
    Price=models.IntegerField(verbose_name="Charge per Hour",null=True)
    Email=models.EmailField(verbose_name="Email")
    Phone=models.IntegerField(verbose_name="Phone No")
    Username=models.CharField(max_length=15,verbose_name="Set Username")
    Password=models.CharField(max_length=15,verbose_name="Set Password")

class Library(models.Model):
    Subject=models.CharField(max_length=100,verbose_name="Subject")
    Books=models.FileField(upload_to='Library', blank=True, null=True, verbose_name="Upload files")

class RequestDemo(models.Model):
    student=models.CharField(max_length=15)
    standard=models.CharField(max_length=10,null=True)
    tutor=models.CharField(max_length=15) 
    subject=models.CharField(max_length=20,null=True) 
    date=models.DateField(null=True)  
    time=models.TimeField(null=True)
    is_complete=models.BooleanField(null=True)

class BookClass(models.Model):
    student=models.CharField(max_length=15)
    standard=models.CharField(max_length=10)
    tutor=models.CharField(max_length=15) 
    subject=models.CharField(max_length=20) 
    date=models.DateField()  
    time=models.TimeField()
    total_time=models.IntegerField()
    price=models.IntegerField()
    is_complete=models.BooleanField(null=True)
    @property
    def amount(self):
        return self.price*self.total_time

class DemoCo(models.Model):
    student=models.CharField(max_length=15)
    standard=models.CharField(max_length=10,null=True)
    tutor=models.CharField(max_length=15) 
    subject=models.CharField(max_length=20,null=True) 
    date=models.DateField(null=True)  
    time=models.TimeField(null=True)
    