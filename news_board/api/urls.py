from django.urls import path

from .views import (PostsView, PostDetail, CommentsView,
                    CommentDetail, VotesUpdate)

urlpatterns = [
        path('posts/', PostsView.as_view()),
        path('posts/<int:pk>/', PostDetail.as_view()),
        path('comments/', CommentsView.as_view()),
        path('comments/<int:pk>/', CommentDetail.as_view()),
        path('votes/<int:pk>/', VotesUpdate.as_view()),
        ]
