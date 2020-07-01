from django.contrib import admin

from .models import Post, Comment


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'author_name', 'amount_of_upvotes')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'content', 'creation_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
