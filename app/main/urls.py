# app/main/urls.py

# django modules
from django.urls import path

# my modules
from app.main.views import home_view, about_view

app_name = 'main'

urlpatterns = [

	# http://127.0.0.1:8000/
    path('', home_view, name='home'),

	# http://127.0.0.1:8000/about/
    path('about/', about_view, name='about'),
    
]