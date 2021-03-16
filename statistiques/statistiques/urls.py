""" statistiques/urls.py """

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('statistiques/', include('apps.main.urls')),
    path('statistiques/admin/', admin.site.urls),
]
