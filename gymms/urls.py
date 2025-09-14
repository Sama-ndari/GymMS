"""
URL configuration for gymms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""
from django.urls import path, include

urlpatterns = [
    path('', include('apps.users.urls')),
    path('', include('apps.core.urls')),
    path('', include('apps.coachs.urls')),
    path('', include('apps.abonnements.urls')),
    path('', include('apps.equipements.urls')),
    path('', include('apps.reservations.urls')),
    path('', include('apps.progres.urls')),
]
