from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_vendor= models.BooleanField(default=False , null= True)
    age = models.IntegerField(default=0)
    salary = models.IntegerField(default=0)
    class Meta:
        db_table  = 'user'
