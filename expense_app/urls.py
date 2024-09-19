from django.urls import path
from . import views

urlpatterns = [
    path('', views.expenses_view, name='expenses'),
    path('add/', views.add_expense_view, name='add_expense'),
]