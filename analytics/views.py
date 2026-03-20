from expenses.models  import  Expense
from budgets.models  import  Budget
from rest_framework.permissions import IsAuthenticated 
from rest_framework.response import Response 
from rest_framework.views import APIView
from django.db.models import Sum
from django.db.models.functions import TruncMonth

class MonthlyExpenseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        expenses = (
            Expense.objects
            .filter(user=request.user)
            .annotate(month=TruncMonth("date"))
            .values("month")
            .annotate(total_amount=Sum("amount"))
            .order_by("month")
        )
        return Response(expenses)

class CategoryWiseExpense(APIView):
    permission_classses = [IsAuthenticated]

    def get(self , request ):
        user = request.user
        expenses = (
            Expense.objects
            .filter(user = user)
            .values("category")
            .annotate(total_expense = Sum("amount"))
            .order_by("-total_expense")
        )
        return Response(expenses)
        
class BudgetAnalytics(APIView):
    permission_classes = [IsAuthenticated]

    def get(self , request):
        user = request.user

        total_expense = Expense.objects.filter(user=user).aggregate(
            Sum("amount"))["amount__sum"] or 0

        total_budget = Budget.objects.filter(user=user).aggregate(
            Sum("amount"))["amount__sum"] or 0

        remaining_balace = total_budget - total_expense

        return Response ({
            "total_expense" : total_expense  ,
            "total_budget"  : total_budget  ,
            "remaining_balace" : remaining_balace ,
        })












































