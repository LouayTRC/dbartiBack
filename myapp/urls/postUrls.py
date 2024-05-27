from django.urls import path
from ..views import postView

urlpatterns = [
    path('add/<str:id>/',postView.addPost, name='add_post'),
    path('get/',postView.getAllPosts, name='getAllPosts'),
    path('delete/<str:idP>/<str:idC>/',postView.delete_comment, name='commentPost'),
    path('delete/<str:id>/',postView.deletePost, name='deletePost'),
    path('comment/<str:idP>/<str:idU>/',postView.create_comment, name='commentPost'),
    path('like/<str:idP>/',postView.likePost, name='likePost'),

]