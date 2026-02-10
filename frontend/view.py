from django.shortcuts import render

def index(request):
    return render(request, "frontend/index.html")

def register_page(request):
    return render(request, "frontend/register.html")