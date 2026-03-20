from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    currency = models.CharField(max_length= 10 , default="INR" ) 

