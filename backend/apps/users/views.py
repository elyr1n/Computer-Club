from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from .forms import SignUpForm, LoginForm, ProfileUpdateForm

User = get_user_model()


@csrf_protect
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()

            messages.success(request, "Аккаунт успешно создан!")

            return redirect("users:login")
    else:
        form = SignUpForm()
        print(form)

    return render(request, "users/sign-up.html", {"form": form})


@csrf_protect
def login_view(request):
    form = LoginForm(data=request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main:home")

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("users:login")


@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Профиль обновлен!")
            return redirect("users:profile")
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, "users/profile.html", {"form": form})


def user_profile_view(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)

    if request.user.is_authenticated and profile_user == request.user:
        return redirect("users:profile")

    return render(request, "users/profile.html", {"profile_user": profile_user})
