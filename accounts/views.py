from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.models import Profile

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        role = request.POST.get("role")

        if not username or not password or not confirm_password or not role:
            messages.error(request, "Please fill in all fields.")
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            Profile.objects.filter(user=user).update(role=role)
            messages.success(request, "Registration successful. Please log in.")
            return redirect("login")
    return render(request, "register.html")