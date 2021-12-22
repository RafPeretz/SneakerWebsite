from django.db import models


class Size(models.Model):
    size_us = models.DecimalField(max_digits=3, decimal_places=1)
    size_eu = models.DecimalField(max_digits=3, decimal_places=1)
    size_uk = models.DecimalField(max_digits=3, decimal_places=1)

  

# Create your models here.
