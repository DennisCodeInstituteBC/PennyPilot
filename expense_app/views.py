from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Expense, Category
from .forms import ExpenseForm
# from django.contrib.auth.decorators import login_required

# Create your views here.

# Dashboard
def dashboard_view(request):
    return render(request, 'dashboard.html')

# Expense table view
def expense_view(request):
    expenses = Expense.objects.filter(user=request.user)
    categories = Category.objects.all()
    return render(request, 'expense.html', {'expenses': expenses, 'categories': categories})

# Add Expense Page
def add_expense_view(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense')

    return render(request, 'add_edit_expense.html', {'categories': categories})

# Edit Expense Page
def edit_expense_page(request, id):
    expense = get_object_or_404(Expense, id=id)
    categories = Category.objects.all()

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense')

    return render(request, 'add_edit_expense.html', {'expense': expense, 'categories': categories})

# Delete Expense
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    expense.delete()
    return redirect('expense')

# Account
def account_view(request):
    return render(request, 'account.html')

# need to look into to fix
# def expense_table_view(request):
#     expenses = Expense.objects.filter(user=request.user)  # Get user's expenses
#     form = ExpenseForm()  # New expense form
#     return render(request, 'expense_table.html', {'expenses': expenses, 'form': form})

# def expense_table_view (request):
#     expense = Expense.objects.filter(user=request.user)
#     form = ExpenseForm()
#     return render(reques, 'expense_table.html', {'expenses': expenses, 'form': form})

# def add_expense(request):
#     if request.method == 'POST':
#         form = ExpenseForm(request.POST)
#         if form.is_valid():
#             expense = form.save(commit=False)
#             expense.user = request.user
#             expense.save()
#             return JsonResponse({'success': True})
#         return JsonResponse({'success': False, 'errors': form.errors})