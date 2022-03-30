from django.urls import path
from apps.friends import views


urlpatterns = [
    path('', views.list_profiles_view, name='list_all_profiles'),
    path('to-invites/', views.invites_list_profiles_view, name='invites_list_profiles'),
    path('invites/', views.invites_received_view, name='invites'),
]