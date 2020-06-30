from django.db import models
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()

class Post(models.Model):
    title = models.CharField(max_length=120)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True,
                                        db_index=True)
    author_name = models.CharField(max_length=60)
    amount_of_upvotes = models.IntegerField(default=0)

class Comment(models.Model):
    author_name = models.CharField(max_length=60)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey('Post', on_delete=models.CASCADE)

class Reply(models.Model):
    author_name = models.CharField(max_length=60)
    content = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    comment_id = models.ForeignKey('Comment', on_delete=models.CASCADE)



