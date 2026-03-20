from .models import Budget
from .serializers import BudgetSerializer 
from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated 


class create_budget(generics.ListCreateAPIView):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self , serializer):
        serializer.save(user=self.request.user)

