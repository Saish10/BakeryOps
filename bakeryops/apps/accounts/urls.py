"""
URLs for the accounts app
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import (
    LoginView, LogoutView, UserView, SignupView
)
router = DefaultRouter()
router.register(r'', UserView, basename="user")

urlpatterns = [
    path("signup", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("", include(router.urls)),
]
