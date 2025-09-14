from django.urls import path
from . import views

urlpatterns = [
    path('coachs/', views.coach_list_view, name='coach_list'),
    path('coachs/create/', views.coach_create_view, name='coach_create'),
    path('coachs/<int:pk>/update/', views.coach_update_view, name='coach_update'),
    path('coachs/<int:pk>/delete/', views.coach_delete_view, name='coach_delete'),
    path('coachs/<int:pk>/activate/', views.coach_activate_view, name='coach_activate'),
]
