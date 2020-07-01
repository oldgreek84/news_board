from django.shortcuts import render, redirect
from django.db.models import Count

from .models import Post, Comment
from .forms import CommentAddForm
# Create your views here.

def index(request):
    posts = Post.objects.all()
    num_comments = Post.objects.annotate(Count('comments'))
    context = {'posts': posts, 'num_comments': num_comments}
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
        form = CommentAddForm()
    context = {'comments': comments,
               'form': form,
               'post': post}
    return render(request, 'comments.html', context)

def add_reply(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    if request.method == 'POST':
        form = CommentAddForm(request.POST)
        if form.is_valid():
            parent_obj = None
            parent_id = int(request.POST.get('parent_id', None))
            if parent_id:
                parent_obj = Comment.objects.get(pk=parent_id)
                if parent_obj:
                    reply = form.save(commit=False)
                    reply.parent = parent_obj
                    reply.post_id = comment.post_id
                    reply.save()
            return redirect('comments', post_id=comment.post_id.pk)
    else:
        form = CommentAddForm(initial={'post_id': comment_id})
    context = {'comment': comment,
               'form': form}
    return render(request, 'reply.html', context)

def upvote_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.send_upvotes()
    return redirect('index')
