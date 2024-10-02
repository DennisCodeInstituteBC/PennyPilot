from django.urls import path
from . import views
from .views import expense_view, add_expense, edit_expense, delete_expense

urlpatterns = [

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Expense
    path('expense/', views.expense_view, name='expense'),
    path('expense/add/', add_expense, name='add_expense'),
    path('expense/edit/<int:expense_id>/', edit_expense, name='edit_expense'),
    # path('expense/delete/<int:id>/', views.delete_expense, name='delete_expense'),


    # Account
    path('account/', views.account_view, name='account')
]