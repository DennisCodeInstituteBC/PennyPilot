from django.shortcuts import render

# Create your views here.
def expenses_view(request):
    return render(request, 'expense_app/dashboard.html')

def add_expense_view(request):
    return render(request, 'expense/add_expense_view.html')