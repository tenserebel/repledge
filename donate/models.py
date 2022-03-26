from django.db import models
from django.core.validators import MaxLengthValidator
from datetime import *

# Create your models here.
class donate(models.Model):
    item_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    category = models.CharField(max_length=200)
    pickup = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=500) 