from django.db import models


# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="DIMAGES")
    about = models.TextField()
    video = models.CharField(max_length=1000)


class ArtForms(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="AIMAGES")
    about = models.TextField()
    video = models.CharField(max_length=1000)


class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="IMAGES")
    about = models.TextField()
    speciality = models.TextField()
    coustomisation = models.BooleanField()
