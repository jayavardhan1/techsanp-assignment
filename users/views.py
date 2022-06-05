from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
# Create your views here.

def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username , password = password)

        if user is not None and user.is_student == True:
            login(request,user)
            return redirect('/students/home/')
        
        elif user is not None and user.is_faculty == True:
            login(request,user)
            return redirect("/teachers/home/")

        

        else:
            return HttpResponse("Please Login")

    return render(request, 'users/login.html')


