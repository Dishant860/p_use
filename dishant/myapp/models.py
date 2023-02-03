from django.db import models

# Create your models here.
class TableEnquiry(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)

class JeCalc(models.Model):
    sel=models.TextField(null=True, blank=True, max_length=50)
    labour=models.FloatField(null=True, blank=True, max_length=50)
    
    price=models.FloatField(max_length=50)
    weight=models.FloatField(max_length=50)
    total=models.FloatField(max_length=50)
    
class Bill(models.Model):
    bname=models.TextField(max_length=50,default="")
    bphone=models.CharField(max_length=10,default="")
    bemail=models.EmailField(max_length=50,default="")
    date=models.DateField(max_length=50,default="")
    cus_id=models.CharField(max_length=50,default="")
    grandtotal=models.CharField(max_length=50,default="")
    
    def __str__(self):
        return self.cus_id
    

    
    

