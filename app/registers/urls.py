from django.urls import path
from .views import LoginPage, LogoutPage

urlpatterns = [
    path("", LoginPage, name='login'),
    path("logout/", LogoutPage, name='login'),
]
