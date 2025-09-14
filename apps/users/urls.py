from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('password-change/', views.password_change_view, name='password_change'),
    path('profile-edit/', views.profile_edit_view, name='profile_edit'),
    
    # Client management (Admin-only views)
    path('', views.user_list_view, name='user_list'),
    path('create/', views.user_create_view, name='user_create'),
    path('<int:pk>/update/', views.user_update_view, name='user_update'),
    path('<int:pk>/approve/', views.user_approve_view, name='user_approve'),
    path('<int:pk>/delete/', views.user_delete_view, name='user_delete'),
    
    # Admin management (Admin-only views)
    path('admins/', views.admin_list_view, name='admin_list'),
    path('admins/create/', views.admin_create_view, name='admin_create'),
    path('admins/<int:pk>/update/', views.admin_update_view, name='admin_update'),
    path('admins/<int:pk>/toggle-status/', views.admin_toggle_status_view, name='admin_toggle_status'),
    path('admins/<int:pk>/delete/', views.admin_delete_view, name='admin_delete'),
]
