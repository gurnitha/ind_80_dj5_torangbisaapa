# config/urls.py

# Modul Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # main
    # http://127.0.0.1:8000/
    path('', include('app.main.urls', namespace='main')),

    # admin
    # http://127.0.0.1:8000/admin
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)