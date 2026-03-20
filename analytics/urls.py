from django.urls import path
from .views import BudgetAnalytics , MonthlyExpenseAPIView , CategoryWiseExpense


urlpatterns = [

    path("budget_analytics/" , BudgetAnalytics.as_view() , name= "BudgetAnalytics") ,
    path("monthly_budget/" , MonthlyExpenseAPIView.as_view() , name = "monthly_analytics" ) , 
    path("category_wise/" , CategoryWiseExpense.as_view() , name = "category_wise" ) ,

]