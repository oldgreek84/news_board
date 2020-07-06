from django.urls import path

from .views import (
        index, comments, add_reply, upvote_post, add_post, MyRegisterFormView, 
        PostCreateView
        )

urlpatterns = [
    path("", index, name="index"),
    # path("accounts/profile/", index, name="index"),
    path("comments/<int:post_id>/", comments, name="comments"),
    path("add_reply/<int:comment_id>/", add_reply, name="add_reply"),
    path("add_post/", add_post, name="add_post"),
    path("upvote/<int:post_id>/", upvote_post, name="upvote_post"),
    path("accounts/register", MyRegisterFormView.as_view(), name="register"),
    path("add/", PostCreateView.as_view(), name="add"),
]
