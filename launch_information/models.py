from django.db import models


class RocketLaunchData(models.Model):
    name    = models.CharField(max_length=70, unique=True)
    date    = models.CharField(max_length=20, null=True)
    time    = models.CharField(max_length=40, null=True)
    country = models.CharField(max_length=50)
    site    = models.CharField(max_length=100)
    des     = models.TextField(null=True)
    live_url = models.URLField(null=True)
    img      = models.ImageField(upload_to = 'static/images/', default = 'images/None/no-img.jpg')


class LaunchSiteData(models.Model):
    country         = models.CharField(max_length=50)
    location        = models.CharField(max_length=130)
    coordinates     = models.CharField(max_length=50)
    no_of_rockets_launched    = models.CharField(max_length=50, null=True)
    heavies_rocket_launched   = models.CharField(max_length=50,null=True)
    highest_altitude_achieved = models.CharField(max_length=15, null=True)
    operational_date          = models.CharField(max_length=20, null=True)


class Facts(models.Model):
    title = models.CharField(max_length=50, unique=True)
    text = models.TextField(unique=True)
    img = models.CharField(max_length=70, null=True)

class Learn(models.Model):
    title = models.CharField(max_length=100, null=True)
    url   = models.CharField(max_length=100,null=True)
    img_url   = models.CharField(max_length=100,null=True)

    img = models.ImageField(upload_to = 'static/images/', default = 'images/None/no-img.jpg')
    des = models.CharField(max_length=200, null=True)

class PreviousLaunchData(models.Model):
    name    = models.CharField(max_length=70, unique=True)
    date    = models.CharField(max_length=20, null=True)
    time    = models.CharField(max_length=40, null=True)
    vehicle = models.CharField(max_length=40, null=True)
    agency  = models.CharField(max_length=40, null=True)
    location= models.CharField(max_length=200, null=True)