from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('some_other_view')  # Redirect after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def signup_view(request):
    return render(request, 'auth_app/signup.html')

def update_password_view(request):
    return render(request, 'auth_app/update_password.html')