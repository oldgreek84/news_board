from django.contrib import admin

from .models import Post, Comment
# from .forms import *

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'author_name', 'amount_of_upvotes')
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'content', 'creation_date')
admin.site.register(Comment, CommentAdmin)
