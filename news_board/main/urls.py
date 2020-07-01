from django.urls import path

from .views import index, comments, add_reply, upvote_post

urlpatterns = [
        path('', index, name='index'),
        path('comments/<int:post_id>', comments, name='comments'),
        path('add_reply/<int:comment_id>/', add_reply, name='add_reply'),
        path('upvote/<int:post_id>/', upvote_post, name='upvote_post'),
        ]
