from django.shortcuts import render
from .forms import CustomUserCreationForm, CustomPasswordChangeForm, CustomPasswordResetForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordChangeView, PasswordResetView, PasswordResetConfirmView

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# Custom password change view

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')


class CustomPasswordChangeDoneView(generic.TemplateView):
    template_name = 'registration/password_change_done.html'


class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = 'registration/password_reset_form.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

