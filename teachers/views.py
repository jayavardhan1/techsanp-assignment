from django.shortcuts import render
from .modelforms import CourseForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/users/login/')
def home(request):
    return render(request,'teachers/home.html')
def addcourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    form =CourseForm()
    context={
        "form":form
    }
    return render(request,"teachers/addcourse.html",context)