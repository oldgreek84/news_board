from rest_framework import serializers

from main.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    """ class serialize Post model to json """

    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ("author_name", "amount_of_upvotes")


class CommentSerializer(serializers.ModelSerializer):
    """ class serialize Comment model to json """

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("author_name", "post_id", "parent")
