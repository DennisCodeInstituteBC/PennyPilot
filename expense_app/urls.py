from django.urls import path
from . import views

urlpatterns = [
     path('dashboard/', views.dashboard_view, name='dashboard'),
    path('expense/', views.expense_view, name='expense'),
    path('account/', views.account_view, name='account')
]