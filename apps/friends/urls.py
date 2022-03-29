from django.urls import path
from apps.friends import views


urlpatterns = [
    path('invites/', views.invites_received_view, name='invites'),
]