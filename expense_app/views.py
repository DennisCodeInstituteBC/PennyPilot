from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Expense, Category, Profile
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


# For graph in dashbaord
from django.shortcuts import render
from .models import Expense
from django.db.models import Sum


# Create your views here.

# Dashboard
@login_required
def dashboard_view(request):
    expenses = Expense.objects.filter(user=request.user).values('category__name').annotate(total=Sum('amount'))
    return render(request, 'dashboard.html', {'expenses': expenses})
    return render(request, 'dashboard.html', context)

# Expense table view

@login_required
def expense_view(request):
    expenses = Expense.objects.filter(user=request.user)
    categories = Category.objects.all() 
    return render(request, 'expense.html', {'expenses': expenses, 'categories': categories})

# Adding Expense
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, "Expense Added Successfully!")
            return redirect('expense_view') 
        else:
            messages.error(request, "Failed to add expense. Please try again.")
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})

# Editing expenses
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, "Expense Updated Successfully!")
            return redirect('expense_view')  
        else:
            messages.error(request, "Failed to update expense. Please try again.")
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'edit_expense.html', {'form': form, 'expense': expense})
    
# Delete Expense
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    
    if request.method == "POST":  
        expense.delete()
        messages.success(request, "Expense Deleted Successfully!")
        return redirect('expense_view')  

    return render(request, 'confirm_delete.html', {'expense': expense})

# Account
@login_required
def account_view(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        profile_image = request.FILES.get('profile_image')
        
        if profile_image:
            if profile.profile_image and profile.profile_image.url != '/media/default.jpg':
                default_storage.delete(profile.profile_image.path)

            profile.profile_image = profile_image
            profile.save()

        return redirect('account')
    
    return render(request, 'account.html', {'profile': profile})
