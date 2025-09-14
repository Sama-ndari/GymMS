from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Information pages
    path('histoire/', views.histoire_view, name='histoire'),
    path('equipe/', views.equipe_view, name='equipe'),
    path('carrieres/', views.carrieres_view, name='carrieres'),
    path('confidentialite/', views.confidentialite_view, name='confidentialite'),
]
