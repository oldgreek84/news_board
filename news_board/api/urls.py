from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import PostsView, PostDetail, CommentsView, CommentDetail, VotesUpdate

urlpatterns = [
    path("posts/", PostsView.as_view()),
    path("posts/<int:pk>/", PostDetail.as_view()),
    path("comments/", CommentsView.as_view()),
    path("comments/<int:pk>/", CommentDetail.as_view()),
    path("votes/<int:pk>/", VotesUpdate.as_view()),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
]
