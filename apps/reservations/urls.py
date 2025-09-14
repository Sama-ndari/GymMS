from django.urls import path
from . import views

urlpatterns = [
    # Admin routes
    path('reservations/', views.reservation_list_view, name='reservation_list'),
    path('reservations/create/', views.reservation_create_view, name='reservation_create'),
    path('reservations/<int:pk>/update/', views.reservation_update_view, name='reservation_update'),
    path('reservations/<int:pk>/delete/', views.reservation_delete_view, name='reservation_delete'),
    
    # Coach routes
    path('coach/reservations/', views.coach_reservation_list_view, name='coach_reservation_list'),
    
    # Client routes
    path('mes-reservations/', views.client_reservation_list_view, name='client_reservation_list'),
    path('mes-reservations/create/', views.client_reservation_create_view, name='client_reservation_create'),
    path('mes-reservations/<int:pk>/update/', views.client_reservation_update_view, name='client_reservation_update'),
    path('mes-reservations/<int:pk>/delete/', views.client_reservation_delete_view, name='client_reservation_delete'),
]
