from django.urls import path
from .views import CreateViewList , ExpenseDetailView

urlpatterns = [

    path("expenses/" , CreateViewList.as_view() ) ,

    path("expenses/<int:pk>/" , ExpenseDetailView.as_view() ) ,

]