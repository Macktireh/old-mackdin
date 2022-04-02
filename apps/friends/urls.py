from django.urls import path
from apps.friends import views


urlpatterns = [
    path('', views.invites_list_profiles_view, name='my_network'),
    path('connections/', views.my_friends_invites_profiles_view, name='my_friends'),
    path('invitation-received/', views.invites_received_view, name='invitation_received'),
    
    path('invitation/accept/', views.accept_invitation, name='accept_invitation'),
    path('invitation/reject/', views.reject_invitation, name='reject_invitation'),
    
    path('send-invitation/', views.send_invitation, name='send_invitation'),
    path('remove-invitation/', views.remove_from_friends, name='remove_invitation'),
]