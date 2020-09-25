from django.urls import path
from . import views

urlpatterns = [
    path('users/<str:username>/', views.tweets_user, name='app-tweets-user'),
    path('hashtags/<str:hashtag>/', views.tweets_hashtag, name='app-tweets-hashtag'),
]