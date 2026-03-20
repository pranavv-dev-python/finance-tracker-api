
from .models import Expense
from rest_framework import serializers

class ExpenseSerialaizers(serializers.ModelSerializer):
    
    class Meta:
        model = Expense 
        fields = "__all__"
        read_only_fields  = ["user"]



