from django.core.management.base import BaseCommand

from main.models import Post


class Command(BaseCommand):
    help = """' docstring """

    def handle(self, *args, **options):
        posts = Post.objects.all()
        for post in posts:
            post.amount_of_upvotes = 0
            post.save()
