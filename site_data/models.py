from django.db import models

class SiteDate(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    logo = models.ImageField(upload_to='site/images',null=True,blank=True)
    address = models.TextField()
    contact = models.TextField()
    email = models.CharField(max_length=100)


