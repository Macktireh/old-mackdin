from django.urls import path
from apps.comments import views

urlpatterns = [
    path('api-data/', views.comment_all_data, name='api-comment'),
    # path('add-comment/', views.add_comment, name='add-comment'),
]