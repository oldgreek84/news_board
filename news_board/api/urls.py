from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import (
        PostList, PostView, PostDetail,
        CommentList, CommentView, CommentDetail, VotesUpdate
        )

urlpatterns = [
    path("posts/all/", PostList.as_view()),
    path("posts/", PostView.as_view()),
    path("posts/<int:pk>/", PostDetail.as_view()),
    path("comments/", CommentList.as_view()),
    path("comments/<int:post_id>/", CommentView.as_view()),
    path("comments/<int:post_id>/<int:pk>/", CommentDetail.as_view()),
    path("votes/<int:pk>/", VotesUpdate.as_view()),
    path("api_auth/", obtain_auth_token, name="api_token_auth"),
]
