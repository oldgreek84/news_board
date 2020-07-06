from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comment, Post

class UserForm(UserCreationForm):
    """ Form for create new user """

    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class CommentAddForm(forms.ModelForm):
    """ create a form to add comment"""

    class Meta:
        model = Comment
        fields = ("content",)

class PostForm(forms.ModelForm):
    """ create a form of new post """

    class Meta:
        model = Post
        fields = ("title", "link")
