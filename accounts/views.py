from django.shortcuts import render, redirect

# forms
from accounts.forms import LoginForm

# services
from accounts.services.services import (
    login_user,
    logout_user
)

from django.contrib import messages

# core
from core.messages import (
    show_form_errors,
    show_error
)

def profil(request):
    return render(request, "accounts/pages/profil.html")

def index(request):
    return render(request, "accounts/index.html")

def logout_view(request):
    logout_user(request)
    return redirect("accounts:login")

def login_view(request):
    # cek apakah sudah login atau belum
    if request.user.is_authenticated:
        return redirect("core:dashboard")
    
    form = LoginForm(request.POST or None)
    
    if request.method == "POST":
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = login_user(request, username, password)
            
            if user:
                # messages.success(request, "Login berhasil")
                return redirect("core:dashboard")
            
            show_error(request, "Username atau password salah")
            return redirect("accounts:login")
        else:
            show_form_errors(request, form)
            
    context = {
        "form": form
    }
            
    return render(request, "accounts/auth/login.html", context)
