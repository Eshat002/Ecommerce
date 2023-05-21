from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    
    email = forms.EmailField(
        
        widget=forms.EmailInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Email'})
    )
    username = forms.CharField(
      
        widget=forms.TextInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
     
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
       
        widget=forms.PasswordInput(attrs={'class': 'form-control mt-2', 'placeholder': 'Confirm Password'})
    )


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    