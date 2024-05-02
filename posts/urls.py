from django.urls import path, include
# from . import views
from django.contrib.auth import views as auth_views
from users import views


urlpatterns = [
   
    path("create", views.post_creation, name="post_creation"),

    path("feed", views.feed, name="feed"),
    path("like", views.like_post, name="like"),
  

]
