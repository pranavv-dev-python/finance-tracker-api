from django.db import models
from django.conf import settings

class Expense(models.Model):
    category_choice = [
        ("food" , "Food") ,
        ("dress" , "Dress") ,
        ("bills" , "Bills") ,
        ("transportaion" , "Transportation")  , 
        ("shopping" , "Shopping") ,
        ("others" , "Others") ,
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE , related_name= "expenses" )
    title = models.CharField(max_length=50 )
    amount = models.DecimalField(max_digits=12 , decimal_places=2)
    category = models.CharField(max_length= 50 , choices=category_choice)
    discription = models.TextField( null=True , blank=True )
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"
    





