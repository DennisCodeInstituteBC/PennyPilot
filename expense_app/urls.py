from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import expense_view, add_expense, edit_expense, delete_expense

urlpatterns = [

    # Dashboard
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Expense
    path('expense/', expense_view, name='expense_view'),
    path('expense/add/', add_expense, name='add_expense'),
    path('expense/edit/<int:expense_id>/', edit_expense, name='edit_expense'),
     path('expense/delete/<int:id>/', views.delete_expense, name='delete_expense'),


    # Account
    path('account/', views.account_view, name='account')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)