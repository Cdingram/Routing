from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Address(models.Model):
    PROVINCES = (
        ('AB', 'Alberta'),
    )

    street = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    province = models.CharField(max_length=2, choices=PROVINCES, default='AB')
    postal_code = models.CharField(max_length=6)
