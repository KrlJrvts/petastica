from django.db import models


# Create your models here.


class Animal(models.Model):
    SHORT_TXT = 128
    TXT = 256
    
    animal_name = models.CharField(
        blank=False,
        null=False,
        max_length=SHORT_TXT
    )
    animal_description = models.TextField(
        blank=False,
        null=False,
        max_length=2560
    )
    animal_weight = models.CharField(
        blank=False,
        null=False,
        max_length=SHORT_TXT
    )
    animal_length = models.CharField(blank=False, null=False, max_length=SHORT_TXT)
    animal_habitat = models.CharField(blank=False, null=False, max_length=SHORT_TXT)
    animal_fact1 = models.CharField(blank=True, null=True, max_length=TXT)
    animal_fact2 = models.CharField(blank=True, null=True, max_length=TXT)
    animal_fact3 = models.CharField(blank=True, null=True, max_length=TXT)
    animal_sound = models.CharField(blank=True, null=True, max_length=SHORT_TXT)
    animal_image1 = models.ImageField(blank=True, null=True, upload_to='')
