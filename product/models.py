from django.db import models

# Create your models here.
class add_categorydb(models.Model):
    user_name = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Picture = models.ImageField(upload_to="pictures/", null=True, blank=True)

class productcategorydb(models.Model):
    Cname = models.CharField(max_length=100, null=True, blank=True)
    Pname = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.FloatField(null=True, blank=True)
    Description = models.CharField(max_length=100, null=True, blank=True)
    Pimage = models.ImageField(upload_to="pictures/", null=True, blank=True)

