from django.urls import path

from .views import PostsView, PostDetail, CommentsView, CommentDetail

urlpatterns = [
        path('posts/', PostsView.as_view()),
        path('posts/<int:pk>/', PostDetail.as_view()),
        path('comments/', CommentsView.as_view()),
        path('comments/<int:pk>/', CommentDetail.as_view()),
        ]
