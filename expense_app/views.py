from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Expense, Category
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Dashboard
def dashboard_view(request):
    return render(request, 'dashboard.html')

# Expense table view

# @login_required
def expense_view(request):
    expenses = Expense.objects.filter()
    categories = Category.objects.all()
    return render(request, 'expense.html', {'expenses': expenses, 'categories': categories})

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()  # Save the expense without linking to a user
            return redirect('expense_view')  # Redirect to the expense page
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})

# adding expenses
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()  # Update the expense
            return redirect('expense_view')  # Redirect to the expense page
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'edit_expense.html', {'form': form, 'expense': expense})

# Delete Expense
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect('expense')

# Account
def account_view(request):
    return render(request, 'account.html')
