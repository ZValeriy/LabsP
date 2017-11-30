from django.shortcuts import render
from lab5RIP.Prods.makelist import listofprs


def list_view(request):
    return render(request, ".\pages\list.html", {'list': listofprs})


def login_view(request):
    return render(request, ".\pages\LogIn.html")


def signup_view(request):
    return render(request, ".\pages\SignUp.html")


def base_view(request):
    return render(request, ".\pages\\base.html")

