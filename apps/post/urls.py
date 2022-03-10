from apps.post import views
from django.urls import path


urlpatterns = [
    path('', views.Post_List_View, name='post_list'),
]