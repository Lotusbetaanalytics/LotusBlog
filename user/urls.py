from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserListCreateView,
    UserAccountRetrieveUpdateDestroyView,
    UserRetrieveUpdateDestroyView,
    PasswordResetView,
    ChangePasswordView,
    ForgotPasswordView
)


urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('account/', UserAccountRetrieveUpdateDestroyView.as_view()),
    path('password-reset/', ChangePasswordView.as_view()),
    path('forgot-password/', ForgotPasswordView.as_view()),
    path('user/<pk>/', UserRetrieveUpdateDestroyView.as_view()),
]