# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class datos(models.Model):
    id= models.AutoField(primary_key = True)
    Altura = models.CharField(max_length = 100)
    Peso = models.CharField(max_length = 100)
    Velocidad = models.CharField(max_length = 100)
    Color = models.CharField(max_length = 100)
