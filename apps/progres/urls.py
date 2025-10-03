from django.urls import path
from . import views

urlpatterns = [
    # Coach routes (main CRUD)
    path('progres/', views.progres_list_view, name='progres_list'),
    path('progres/create/', views.progres_create_view, name='progres_create'),
    path('progres/<int:pk>/', views.progres_detail_view, name='progres_detail'),
    path('progres/<int:pk>/update/', views.progres_update_view, name='progres_update'),
    path('progres/<int:pk>/delete/', views.progres_delete_view, name='progres_delete'),
    
    # Admin read-only
    path('admin/progres/', views.admin_progres_list_view, name='admin_progres_list'),
    path('admin/progres/<int:pk>/', views.admin_progres_detail_view, name='admin_progres_detail'),
    
    # Client routes
    path('mes-progres/', views.client_progres_list_view, name='client_progres_list'),
    path('mes-progres/<int:pk>/', views.client_progres_detail_view, name='client_progres_detail'),
]
