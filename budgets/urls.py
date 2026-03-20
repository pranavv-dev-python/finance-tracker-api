from django.urls import path
from .views import create_budget

urlpatterns = [
    path('budget/' , create_budget.as_view() , name="budget" )
]

