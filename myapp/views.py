from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


@login_required(login_url='login')
def homePage(request):
    return render(request, 'home.html')


def signup_view(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Basic validation
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('signup')  # Adjust as needed

        try:
            # Create user
            my_user = User.objects.create_user(
                username=uname, email=email, password=pass1)
            messages.success(request, "Account created successfully")
            return redirect('login')  # Adjust as needed
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('signup')  # Adjust as needed
    else:
        return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'login.html')


def dashboard_view(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('login')
