from django.urls import path
from . import views

urlpatterns = [
    # Admin routes
    path('abonnements/', views.abonnement_list_view, name='abonnement_list'),
    path('abonnements/create/', views.abonnement_create_view, name='abonnement_create'),
    path('abonnements/<int:pk>/update/', views.abonnement_update_view, name='abonnement_update'),
    path('abonnements/<int:pk>/delete/', views.abonnement_delete_view, name='abonnement_delete'),
    
    # Coach routes
    path('coach/abonnements/', views.coach_abonnement_list_view, name='coach_abonnement_list'),
    
    # Client routes
    path('mes-abonnements/', views.client_abonnement_list_view, name='client_abonnement_list'),
    path('mes-abonnements/create/', views.client_abonnement_create_view, name='client_abonnement_create'),
]
