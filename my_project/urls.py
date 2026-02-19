"""
URL configuration for my_project project.
Handles routing for Admin, Allauth, Summernote, and the Center app.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('summernote/', include('django_summernote.urls')),
    path("", include("center.urls")),
]
