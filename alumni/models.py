# -*- coding : utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from desescuela.models import Cinta, Batch
class AlumniManager(models.Manager):

    def active(self):
        return Alumni.objects.filter(is_active=True)

    def inactive(self):
        return Alumni.objects.filter(is_active=False)


class Alumni(models.Model):

    class Meta:
        verbose_name = "Alumni"
        verbose_name_plural = "Alumnis"

    #Attributes
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=30)
    tel = models.CharField(max_length=15)
    mail = models.EmailField(max_length=500)
    is_active = models.BooleanField(default=True)

    #manager
    objects = AlumniManager()

    #Relations
    cinta = models.ForeignKey(Cinta, related_name='cinta_alumni')
    batch = models.ForeignKey(Batch, related_name='batch_alumni')


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.mail == "paco.ocampo@mail.com" :
            raise Exception("El mail es invalido")
            return
        super(Alumni, self).save(*args, **kwargs)
