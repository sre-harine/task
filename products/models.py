from django.db import models

# Create your models here.
class Product(models.Model):
    skuName=models.CharField(max_length=45)
    skuCategory=models.CharField(max_length=20)
    price=models.FloatField()
class Meta:
    db_table='products'