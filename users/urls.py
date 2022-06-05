from .views import LoginView
from django.urls import path

app_name = "users"

urlpatterns = [
    path("login/",LoginView,name="login")
]
