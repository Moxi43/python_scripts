from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from .forms import UserCreationForm
from .models import User
from blog.models import Blog


def home(request):
    return HttpResponse("Home page")


def login(request):
    if request.POST:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user = auth.authenticate(password=password, username=username)
        if user is not None:
            auth.login(request, user)
            return redirect("/blog/")
        else:
            return render(request, "authorization/login.html")
    else:
        return render(request, "authorization/login.html")


def logout(request):
    auth.logout(request)
    return redirect("/authorization/login")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            first_password = form.cleaned_data.get("password1")
            second_password = form.cleaned_data.get("password2")
            if first_password == second_password:
                user = authenticate(request, username=username, password=second_password)
                User.objects.create_user(username=username, password=second_password,)
                blog = Blog(header_text="MyBlog")
                blog.save()

            else:
                return HttpResponseRedirect('/authorization/register/')

            return HttpResponseRedirect('/authorization/login/')
    else:
        form = UserCreationForm()

    return render(request, "authorization/register.html", {"form": form})
