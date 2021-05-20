from django.contrib import admin
from .models import Article, Tag, Comment, Like_post, Like_comment

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'updated_at']
    list_filter = ['author', 'tags']
    search_fields = ['title', 'content', 'tags']
    fields = ['id', 'title', 'author', 'tags', 'content', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at', 'id', 'author']


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag', 'created_at', 'updated_at']
    list_filter = ['tag']
    search_fields = ['tag']
    fields = ['id', 'tag', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'article', 'comment', 'author', 'created_at', 'updated_at']
    list_filter = ['article', 'author']
    search_fields = ['article', 'comment', 'author']
    fields = ['id', 'article', 'comment', 'author', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'author', 'updated_at']

class PostLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'user']
    list_filter = ['user']
    search_fields = ['user']
    fields = ['id', 'post', 'user']
    readonly_fields = ['id']

class CommentLikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'user']
    list_filter = ['user']
    search_fields = ['user']
    fields = ['id', 'comment', 'user']
    readonly_fields = ['id']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like_comment, CommentLikeAdmin)
admin.site.register(Like_post, PostLikeAdmin)
