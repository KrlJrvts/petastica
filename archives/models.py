from django.db import models


# Create your models here.


class Animal(models.Model):
    animal_name = models.CharField(blank=False, null=False, max_length=128)
    animal_description = models.CharField(blank=False, null=False, max_length=2000)
    animal_weight = models.CharField(blank=False, null=False, max_length=128)
    animal_length = models.CharField(blank=False, null=False, max_length=128)
    animal_habitat = models.CharField(blank=False, null=False, max_length=128)
    animal_fact1 = models.CharField(blank=True, null=True, max_length=256)
    animal_fact2 = models.CharField(blank=True, null=True, max_length=256)
    animal_fact3 = models.CharField(blank=True, null=True, max_length=256)
    animal_sound = models.CharField(blank=True, null=True, max_length=128)
    animal_image1 = models.CharField(blank=True, null=True, max_length=128)
    animal_image2 = models.CharField(blank=True, null=True, max_length=128)
