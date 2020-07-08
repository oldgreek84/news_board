from django.shortcuts import render, redirect
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Post, Comment
from .forms import CommentAddForm, UserForm, PostForm


def index(request):
    """ function render html template for index page"""

    posts = Post.objects.all()
    context = {"posts": posts, "title": "Main Page"}
    return render(request, "index.html", context)


@login_required
def comments(request, post_id):
    """ function render html template for comments page"""

    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    if request.method == "POST":
        form = CommentAddForm(request.POST)
        if form.is_valid():

            comment = form.save(commit=False)
            comment.post_id = post
            comment.author_name = request.POST.get('author_name')
            comment.save()
            return redirect("comments", post_id=post_id)
    else:
        form = CommentAddForm(
                initial={"author_name": request.GET.get("author_name")})
    context = {"comments": comments,
               "form": form,
               "post": post,
               "title": "Comments"}
    return render(request, "comments.html", context)


@login_required
def add_post(request):
    """ func added new post """

    pass


@login_required
def add_reply(request, comment_id):
    """ function render html template for reply page"""

    comment = Comment.objects.get(pk=comment_id)
    if request.method == "POST":
        form = CommentAddForm(request.POST)
        if form.is_valid():
            parent_obj = None
            parent_id = int(request.POST.get("parent_id", None))
            if parent_id:
                parent_obj = Comment.objects.get(pk=parent_id)
                if parent_obj:
                    reply = form.save(commit=False)
                    reply.parent = parent_obj
                    reply.author_name = request.POST.get('author_name')
                    reply.post_id = comment.post_id
                    reply.save()
            return redirect("comments", post_id=comment.post_id.pk)
    else:
        form = CommentAddForm(initial={"post_id": comment_id})
    context = {"comment": comment, "form": form, "title":"Add reply"}
    return render(request, "reply.html", context)


@login_required
def upvote_post(request, post_id):
    """ upvote_post(post_id:int) -> None """

    post = Post.objects.get(pk=post_id)
    post.upvote(request.user)
    return redirect("index")


class PostCreateView(LoginRequiredMixin, CreateView):
    """ class create new post """

    template_name = "add_post.html"
    form_class = PostForm
    success_url = reverse_lazy("index") 

    def form_valid(self, form):
        form.instance.author_name = self.request.user.username
        return super(PostCreateView, self).form_valid(form)


class MyRegisterFormView(FormView):
    """ create view for registration new user """

    form_class = UserForm
    success_url = "login/"
    template_name = "registration/register.html"

    def form_valid(self, form):
        """ check form to  valid """

        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        """ check form to  invalid """
        
        return super(MyRegisterFormView, self).form_invalid(form)
