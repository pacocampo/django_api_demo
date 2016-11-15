from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cinta(models.Model):

    class Meta:
        verbose_name = "Cinta"
        verbose_name_plural = "Cintas"

    color = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.color
    

class Batch(models.Model):

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batchs"

    #Attributes
    name = models.CharField(max_length=255)
    start_date = models.DateField(auto_now_add=False)
    end_date = models.DateField(auto_now_add=False)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    