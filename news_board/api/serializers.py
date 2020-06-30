from rest_framework import serializers

from main.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # fileds = ('id', 'title', 'link', 'creation_date',
        #           'author_name', 'amount_of_upvotes')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
