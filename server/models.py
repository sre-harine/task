from django.db import models

# Create your models here.
class Userreg(models.Model):
    phone=models.CharField(max_length=20)
    password=models.CharField(max_length=25)
    dob=models.DateField()
class Meta:
    db_table='users'