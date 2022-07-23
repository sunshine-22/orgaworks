from django.utils import timezone
from django.db import models



# Create your models here.
class Employee(models.Model):
    Fullname=models.CharField(max_length=100)
    Email=models.EmailField(primary_key=True)
    phone=models.IntegerField()
    Role=models.CharField(max_length=100)
    Country=models.CharField(max_length=100)
    State=models.CharField(max_length=50)
    Zipcode=models.IntegerField()
    Experience=models.IntegerField()
    Linkedin=models.CharField(max_length=300)
    Employeeid=models.CharField(max_length=100)
    Resume = models.FileField(upload_to='Resumes')
    Employee_Status=models.CharField(default="Not Approved",max_length=100)

class products(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    category_choices = ( ('Fruits',"Fruits"),('Exotics',"Exotics"),('vegetables',"Vegetables"))
    
    category =models.CharField(max_length=20,
                  choices=category_choices )
    productlinkImage=models.ImageField(upload_to='products')
    lowest_prices = models.TextField(max_length=10)
    communityfarm=models.CharField(max_length=10000)
    greendna=models.CharField(max_length=10000)
    healthybuddha=models.CharField(max_length=10000)
    organiceraa=models.CharField(max_length=10000)
    freshfarm=models.CharField(max_length=10000)
    def __str__(self):
        return self.name



class contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)    
    message = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name
    
class review(models.Model):
    name=models.CharField(max_length=1000)
    email=models.EmailField()
    review=models.CharField(max_length=10000000)
    product=models.CharField(max_length=1000)
    

    
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    
    title = models.CharField(max_length=255, blank=True)
    blogImage = models.ImageField(upload_to='blogs')
    content = models.TextField(max_length=10000, blank=True)
    def __str__(self):
        return str(self.title)
