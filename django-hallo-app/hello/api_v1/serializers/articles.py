from rest_framework import serializers
from article.models import Article


class ArticleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'author', 'created_at')
        read_only_fields = ('author', 'id')

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'created_at')
        read_only_fields = ('author', 'id')
