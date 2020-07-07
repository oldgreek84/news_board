from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (
    ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, 
)
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from main.models import Post, Comment
from .serializers import CommentSerializer, PostSerializer


class PostList(ListAPIView):
    """ class realise GET method for Post model """

    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostView(ListCreateAPIView):
    """ class realise methods GET, POST for Post model """

    permission_classes = (IsAuthenticated,)   

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        """ method add author name to model"""

        serializer.save(author_name=self.request.user.username)
        return Response(serializer.data)


class PostDetail(RetrieveUpdateDestroyAPIView):
    """ GET, PUT, PATCH, DELETE methods for post """

    permission_classes = (IsAuthenticated,)   
    serializer_class = PostSerializer

    def get_queryset(self):
        """ method returned objects where author is current user """

        return Post.objects.filter(author_name=self.request.user.username)


class CommentList(ListAPIView):
    """ class reailse GET method for Comment model """

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentView(ListCreateAPIView):
    """ GET, POST methods for comment """

    permission_classes = (IsAuthenticated,)   

    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        """ method return queryset of Comment """

        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        """ method add author name to model and check correct
            parent_id, post_id"""
        
        post_id = self.request.data.get('post_id')
        parent = self.request.data.get('parent')

        if parent: 
            obj = get_object_or_404(Comment, post_id=post_id, pk=parent)
        data = {
            'author_name': self.request.user.username,
            'parent_id': parent,
            'post_id_id': post_id
            }
        if serializer.is_valid(raise_exception=True):
            serializer.save(**data)
        return Response(serializer.data)


class CommentDetail(RetrieveUpdateDestroyAPIView):
    """ GET, PUT, PATCH, DELETE methods for comment """

    permission_classes = (IsAuthenticated,)   
    serializer_class = CommentSerializer

    def get_queryset(self):
        """ doc """
        
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(author_name=self.request.user.username, 
                post_id=post_id)


class VotesUpdate(APIView):
    """ class realise change count of  upvotes in model"""

    permission_classes = (IsAuthenticated,)   

    def patch(self, request, pk):
        """ method find model by pk, and change model upvotes"""

        print(pk)
        instance = get_object_or_404(Post, pk=pk)
        instance.upvote(request.user)
        serializer = PostSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
