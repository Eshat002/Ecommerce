from django.shortcuts import render, redirect
from .form import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import logout


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop')  # Replace 'home' with your desired URL name
            else:
                messages.error(request, 'Failed to log in.')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})


 

def login_view(request):
 
    error_message = ''
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop')  # Replace 'home' with your desired redirect URL
            else:
                error_message = 'Invalid username or password'
        else:
            error_message = 'Invalid username or password'
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form, 'error_message': error_message})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/account/login/')  # Replace 'home' with your desired redirect URL after logout

    return render(request, 'logout.html')
