from unicodedata import name
from django.urls import path,include
from . import views
urlpatterns = [
    path('home/',views.home),
    path('addcourse/',views.addcourse ,name="addcourse")
]