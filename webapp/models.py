from django.db import models

# Create your models here.
class contactdb(models.Model):
    Yname = models.CharField(max_length=100, null=True, blank=True)
    Yemail = models.CharField(max_length=100, null=True, blank=True)
    Yphone = models.IntegerField(null=True, blank=True)
    Ymessage = models.CharField(max_length=500, null=True, blank=True)

class userdb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    UserEmail = models.CharField(max_length=100, null=True, blank=True)
    UserPassword = models.CharField(max_length=100, null=True, blank=True)
    UserCpassword = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):
    Productname = models.CharField(max_length=100, null=True, blank=True)
    Productprice = models.FloatField(null=True, blank=True)
    Productquantity = models.IntegerField(null=True, blank=True)
    Totalprice = models.IntegerField(null=True, blank=True)