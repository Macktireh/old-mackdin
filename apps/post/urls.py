from apps.post import views
from django.urls import path


urlpatterns = [
    path('', views.Post_List_View, name='post_list'),
    path('like/', views.like_post, name='like_post'),
    # path('<myid>/like/', views.like_post, name='like_post'),
]