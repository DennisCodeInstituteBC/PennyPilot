from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    return render(request, 'auth_app/login.html')

def signup_view(request):
    return render(request, 'auth_app/signup.html')

def update_password_view(request):
    return render(request, 'auth_app/update_password.html')