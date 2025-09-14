from django.urls import path
from . import views

urlpatterns = [
    # Admin routes
    path('equipements/', views.equipement_list_view, name='equipement_list'),
    path('equipements/create/', views.equipement_create_view, name='equipement_create'),
    path('equipements/<int:pk>/update/', views.equipement_update_view, name='equipement_update'),
    path('equipements/<int:pk>/delete/', views.equipement_delete_view, name='equipement_delete'),
    
    # Coach routes
    path('coach/equipements/', views.coach_equipement_list_view, name='coach_equipement_list'),
]
