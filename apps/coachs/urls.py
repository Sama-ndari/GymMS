from django.urls import path
from . import views

urlpatterns = [
    # Admin coach management
    path('coachs/', views.coach_list_view, name='coach_list'),
    path('coachs/create/', views.coach_create_view, name='coach_create'),
    path('coachs/<int:pk>/update/', views.coach_update_view, name='coach_update'),
    path('coachs/<int:pk>/delete/', views.coach_delete_view, name='coach_delete'),
    path('coachs/<int:pk>/activate/', views.coach_activate_view, name='coach_activate'),
    
    # Admin coach-client assignments
    path('coach-clients/', views.coach_clients_view, name='coach_clients'),
    path('coachs/<int:coach_pk>/assign-client/', views.assign_client_to_coach_view, name='assign_client_to_coach'),
    path('coach-assignments/<int:assignment_pk>/unassign/', views.unassign_client_from_coach_view, name='unassign_client_from_coach'),
    
    # Client views - coach requests
    path('my-coaches/', views.client_my_coaches_view, name='client_my_coaches'),
    path('request-coach/<int:coach_pk>/', views.client_request_coach_view, name='client_request_coach'),
    path('cancel-request/<int:assignment_pk>/', views.client_cancel_request_view, name='client_cancel_request'),
    
    # Coach views - client management
    path('my-clients/', views.coach_my_clients_view, name='coach_my_clients'),
    path('approve-request/<int:assignment_pk>/', views.coach_approve_request_view, name='coach_approve_request'),
    path('reject-request/<int:assignment_pk>/', views.coach_reject_request_view, name='coach_reject_request'),
    path('deassign-client/<int:assignment_pk>/', views.coach_deassign_client_view, name='coach_deassign_client'),
]
