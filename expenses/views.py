from .models import Expense
from .serializers import ExpenseSerialaizers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CreateViewList(generics.ListCreateAPIView):
    serializer_class = ExpenseSerialaizers 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self , serializer):
        serializer.save(user=self.request.user)

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ExpenseSerialaizers
    permission_classes = [IsAuthenticated]

    def get_querset(self):
        return Expense.objects.filter(user=self.request.user)


