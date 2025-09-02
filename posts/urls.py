from django.urls import path
from . import views
urlpatterns = [
    path('create_post/',views.Post_create,name="Post_create"),
    path('all_posts/',views.feed,name="all_posts"),
    path('like/',views.like,name="likes"),
]