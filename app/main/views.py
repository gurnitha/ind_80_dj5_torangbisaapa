# app/main/views.py

# django modules
from django.shortcuts import render


# Create your views here.

def home_view(request):
	return render(request, 'main/index.html')


def about_view(request):
	return render(request, 'main/about.html')