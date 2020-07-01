from django import forms

from .models import Comment

class CommentAddForm(forms.ModelForm):
    class Meta:
        model = Comment
<<<<<<< HEAD
        # fields = ('author_name', 'content')
        fields = '__all__'
        widgets = {'post_id': forms.HiddenInput}
=======
        fields = ('content', 'author_name')

>>>>>>> 6804854fa8db6738f4e8dea7419f6ac8b3d62c1c
