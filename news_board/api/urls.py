from django.urls import path

from .views import PostsView, PostDetail, CommentsView

urlpatterns = [
        path('posts/', PostsView.as_view()),
        path('post_detail/<int:pk>', PostDetail.as_view()),
        path('<int:pk>/comments/', CommentsView.as_view())
        ];
