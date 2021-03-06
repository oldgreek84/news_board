from django.db import models, IntegrityError
from django.contrib import messages
from django.utils import timezone


class Post(models.Model):
    """ create db model of post """

    title = models.CharField(max_length=120)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True, db_index=True)
    author_name = models.CharField(max_length=60)
    amount_of_upvotes = models.IntegerField(default=0)

    class Meta:
        ordering = ("-creation_date",)

    def __str__(self):
        return f"Post {self.id} by {self.author_name}"

    def votes_count(self):
        return self.votes.all().count()

    def upvote(self, user):
        try:
            self.votes.create(user=user, post=self)
            self.amount_of_upvotes += 1
            self.save()
        except IntegrityError:
            return 'already  upvotes'
        return 'ok'


class Comment(models.Model):
    """ create db model of comment """

    author_name = models.CharField(max_length=60)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey(
        "Post", related_name="comments", on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="replies", on_delete=models.CASCADE
    )

    class Meta:
        ordering = ("-creation_date",)

    def __str__(self):
        return f"{self.author_name} to post {self.post_id}"


class Vote(models.Model):

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='votes', 
            on_delete=models.CASCADE)

    class Meta:
        unique_together = [('post'), ('user')]
