from django import forms

from .models import Comment


class CommentAddForm(forms.ModelForm):
    ''' create a form to add comment'''

    class Meta:
        model = Comment
        fields = ('content', 'author_name')
