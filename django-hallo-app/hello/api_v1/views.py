from django.http import Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from .serializers.articles import ArticleDetailSerializer, ArticleListSerializer
from article.models import Article
from rest_framework.response import Response

# class ArticleListView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleListSerializer
#
#
# class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ArticleDetailSerializer
#     queryset = Article.objects.all()

class ArticleListView(APIView):

    # get для вывода всех статей
    def get(self, request, *args, **kwargs):
        objects = Article.objects.all()
        serializer = ArticleListSerializer(objects, many=True)
        return Response(serializer.data)

    # post для создания одной статьи, ибо пк не требуется
    def post(self, request, *args, **kwargs):
        serializer = ArticleDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetailView(APIView):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=self.kwargs.get('pk'))
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=self.kwargs.get('pk'))
        serializer = ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=self.kwargs.get('pk'))
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








