from django.shortcuts import render
from teachers.models import Course
# Create your views here.
def home(request):
    courses = Course.objects.all()
    context={
        "courses":courses
    }
    return render(request,"students/home.html",context)
def course(request):
    return render(request,"students/course.html")