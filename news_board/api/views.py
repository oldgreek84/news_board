from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     UpdateAPIView)
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from main.models import Post, Comment
from .serializers import CommentSerializer, PostSerializer


class PostsView(ListCreateAPIView):
    '''
    class realise get, post methods
    '''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        ''' method add author name to model'''
        author_name = self.request.data.get('author_name')
        return serializer.save(author_name=author_name)

class PostDetail(RetrieveUpdateDestroyAPIView):
    ''' class realise put, patch, delete methods'''
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentsView(ListCreateAPIView):
    ''' class realise get, post method  to models'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(RetrieveUpdateDestroyAPIView):
    '''class realise put, patch, delete methods'''
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class VotesUpdate(APIView):
    ''' class realise change count of  upvotes in model'''

    def patch(self, request, pk):
        ''' method find model by pk, and change model upvotes'''
        model = Post.objects.get(pk=pk)
        data = {'amount_of_upvotes': model.amount_of_upvotes + 1}
        serializer = PostSerializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
