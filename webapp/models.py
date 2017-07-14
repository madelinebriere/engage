# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 250)

class Charity(models.Model):
    name = models.CharField(max_length = 500)
    description = models.CharField(max_length = 1000)
    votes = models.IntegerField(default=0)
    class Meta:
        ordering = ('-votes', 'name')

class Donation(models.Model):
    name = models.CharField(max_length = 500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=13, decimal_places=2, default=0)

