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

    def __str__(self):
        return f'Post {self.id} by {self.author_name}'

    def send_upvotes(self):
        self.amount_of_upvotes += 1
        self.save()

class Comment(models.Model):
    author_name = models.CharField(max_length=60)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey('Post',
                                related_name='comments',
                                on_delete=models.CASCADE)
    parent = models.ForeignKey('self',
                               null=True,
                               blank=True,
                               related_name='replies',
                               on_delete=models.CASCADE)

    class Meta:
        ordering = ('-creation_date',)

    def __str__(self):
        return f'{self.author_name} to post {self.post_id}'

class Reply(models.Model):
    author_name = models.CharField(max_length=60)
    content = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    comment_id = models.ForeignKey('Comment', on_delete=models.CASCADE)
