from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, PasswordResetForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'age',)
    
    
class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email', 'age',)


# Customizing the forms


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'background-color: #0d1117; border: 1px solid #30363d; color: #c9d1d9;',
            'placeholder': 'Old Password'
        })
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'background-color: #0d1117; border: 1px solid #30363d; color: #c9d1d9;',
            'placeholder': 'New Password'
        })
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'background-color: #0d1117; border: 1px solid #30363d; color: #c9d1d9;',
            'placeholder': 'Confirm New Password'
        })
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.CharField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'style': 'background-color: #0d1117; border: 1px solid #30363d; color: #c9d1d9;',
            'placeholder': 'Confirm New Password'
        })
    )