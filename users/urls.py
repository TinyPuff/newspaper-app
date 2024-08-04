from django.urls import path
from .views import SignUpView, CustomPasswordChangeView, CustomPasswordChangeDoneView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
]