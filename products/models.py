from django.db import models
from datetime import datetime
from size.models import Size
from category.models import Category
from company.models import Company

class Sneakers(models.Model):
    size = models.ForeignKey(Size,on_delete=models.PROTECT)
    company = models.ForeignKey(Company,on_delete=models.PROTECT)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
# Create your models here.

def __str__(self):
    return self.sneakers.title
