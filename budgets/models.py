from django.db import models
from django.conf import settings
# Create your models here.

class Budget(models.Model):
    category = [
    ("food" , "Food") ,
    ("dress" , "Dress") ,
    ("bills" , "Bills") ,
    ("transportaion" , "Transportation")  , 
    ("shopping" , "Shopping") ,
    ("others" , "Others") ,
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name= "budgets" )
    amount = models.DecimalField(max_digits=10 , decimal_places=2 )
    category = models.CharField(max_length= 50 , choices=category)
    month = models.DateField()


