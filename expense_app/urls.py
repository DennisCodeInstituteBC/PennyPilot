from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),
    # Expense
    path('expense/', views.expense_view, name='expense'),
    path('expense/add/', views.add_expense_view, name='add_expense'),
    # path('expense/edit/<int:id>/', views.edit_expense_page, name='edit_expense'),
    # path('expense/delete/<int:id>/', views.delete_expense, name='delete_expense'),
    # Account
    path('account/', views.account_view, name='account')
]