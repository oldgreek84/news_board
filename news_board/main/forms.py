from django import forms

from .models import Comment

class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = ('author_name', 'content')
        fields = '__all__'
        widgets = {'post_id': forms.HiddenInput}
