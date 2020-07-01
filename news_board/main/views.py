from django.shortcuts import render, redirect
from django.db.models import Count

from .models import Post, Comment
from .forms import CommentAddForm
# Create your views here.

def index(request):
    posts = Post.objects.all()
    num_comments = Post.objects.annotate(Count('comment'))
    context = {'posts': posts, 'num_comments': len(num_comments)}
    return render(request, 'index.html', context)

def comments(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    if request.method == 'POST':
        form = CommentAddForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = post
            comment.save()
            return redirect('comments', post_id=post_id)
    else:
        form = CommentAddForm(instance=post)
    context = {'comments': comments, 'form': form,
               'post': post}
    return render(request, 'comments.html', context)

def add_reply(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'POST':
        form = CommentAddForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('comments', post_id=comment_id)
    else:
        form = CommentAddForm(initial={'post_id': comment_id})
    context = {'comment': comment,
               'form': form}
    return render(request, 'reply.html', context)

