from __future__ import unicode_literals

from django.db import models
from desescuela.models import Cinta

# Create your models here.
class Sensei(models.Model):

    class Meta:
        verbose_name = "Sensei"
        verbose_name_plural = "Senseis"

    #attributes
    alias = models.CharField(max_length=255)
    pic = models.ImageField(upload_to="senseis/bio/")
    tel = models.CharField(max_length=15)
    mail = models.CharField(max_length=255)

    #relations
    cinta = models.ManyToManyField(Cinta)
    def __str__(self):
        return self.alias

