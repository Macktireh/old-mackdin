from django.urls import path
from apps.comments import views

app_name = 'comments'

urlpatterns = [
    # path('api-data/', views.comment_all_data, name='api-comment'),
    path('add-comment/', views.add_comment, name='add-comment'),
]