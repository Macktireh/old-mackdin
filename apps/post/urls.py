from apps.post import views
from django.urls import path


urlpatterns = [
    path('', views.post_create_list_view, name='post_list'),
    path('like/', views.like_post, name='like_post'),
    # path('<myid>/like/', views.like_post, name='like_post'),
]