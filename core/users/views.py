from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # import your new form
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "users/success.html")  # or redirect to login
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})
def custom_login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_doctor:
                return redirect("doctor_dashboard")
            elif user.is_patient:
                return redirect("patient_dashboard")
            else:
                return redirect("login")  # fallback for other types
        else:
            return render(request, "users/login.html", {"error": "Invalid credentials"})
    return render(request, "users/login.html")

@login_required
def patient_dashboard(request):
    return render(request, "users/patient_dashboard.html")

@login_required
def doctor_dashboard(request):
    return render(request, "users/doctor_dashboard.html")
def custom_logout_view(request):
    logout(request)
    return redirect("logged_out")

def logged_out(request):
    return render(request, "users/logged_out.html")

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # Ensure the user is logged in
def video_call(request, room_name):
    # Ensure the user is allowed to access this room (e.g., only patient and doctor can join)
    if request.user.is_authenticated:
        return render(request, "users/video_call.html", {"room_name": room_name})
    else:
        return redirect('login')