from django.urls import path

from .views import PostsView, PostDetail, CommentsView, CommentDetail

urlpatterns = [
        path('posts/', PostsView.as_view()),
        path('posts/detail/<int:pk>', PostDetail.as_view()),
        path('comments/<int:pk>', CommentsView.as_view()),
        path('comments/detail/<int:pk>', CommentDetail.as_view()),
        ]
