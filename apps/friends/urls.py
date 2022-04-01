from django.urls import path
from apps.friends import views


urlpatterns = [
    # path('', views.list_profiles_view, name='list_all_profiles'),
    path('', views.invites_list_profiles_view, name='my_network'),
    path('connections/', views.my_friends_invites_profiles_view, name='my_friends'),
    path('invite-connect/invites/', views.invites_received_view, name='invites'),
    
    path('send-invitation', views.send_invitation, name='send_invitation'),
    path('remove-invitation', views.remove_from_friends, name='remove_invitation'),
]