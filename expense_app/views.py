from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Expense, Category
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

# For graph in dashbaord
from django.shortcuts import render
from .models import Expense
from django.db.models import Sum


# Create your views here.

# Dashboard
def dashboard_view(request):
    # Fetch and group expenses by category
    expenses = Expense.objects.filter(user=request.user).values('category__name').annotate(total=Sum('amount'))

    # Extract categories and total spendings
    categories = [expense['category__name'] for expense in expenses]
    total_spendings = [expense['total'] for expense in expenses]

    context = {
        'categories': categories,
        'total_spendings': total_spendings,
    }

    return render(request, 'dashboard.html', context)

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
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()  # Save the expense without linking to a user
            return redirect('expense_view') 
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})

# adding expenses
def edit_expense(request, expense_id):
    # Get the expense by its ID without checking ownership
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()  # Update the expense
            return redirect('expense_view')  # Redirect to the expense list
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'edit_expense.html', {'form': form, 'expense': expense})
# Delete Expense
def delete_expense(request, id):
    # Get the expense by its ID without checking ownership
    expense = get_object_or_404(Expense, id=id)
    
    if request.method == "POST":  # Optional: confirm deletion via POST request
        expense.delete()  # Delete the expense
        return redirect('expense_view')  # Redirect to the expense list

    return render(request, 'confirm_delete.html', {'expense': expense})  # Optional confirmation page

# Account
def account_view(request):
    return render(request, 'account.html')
