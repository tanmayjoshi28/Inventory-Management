from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def start_page(request):
    return render(request, 'users/login.html')


def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("inventory:homepage"))
        else:
            context["error"] = "Provide Valid Credentials"
            return render(request, "users/login.html", context)
    else:
        return render(request, "users/login.html", context)




