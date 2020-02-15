# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Gtin(models.Model):
    objects = None
    gtin_number = models.CharField(max_length=30)
    product_name = models.CharField(max_length=30)

    # def __str__(self):
    #     return self.gtin_number

    class Meta:
        verbose_name_plural = "GTIN NUMBER"
        verbose_name = "GTIN NUMBER"
