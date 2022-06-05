from django.urls import path,include
from students import views
urlpatterns = [
    path("home/",views.home,name="home"),
    path("course/",views.course,name="course")
]