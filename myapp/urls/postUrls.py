from django.urls import path
from ..views import postView

urlpatterns = [
    path('add/',postView.addPost, name='add_post'),
    path('get/',postView.getAllPosts, name='getAllPosts'),
    path('delete/<str:id>/',postView.deletePost, name='deletePost'),

]