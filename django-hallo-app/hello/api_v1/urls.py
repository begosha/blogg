from django.urls import path, include
from .views import ArticleListView, ArticleDetailView
app_name = 'api_v1'


article_urls = [
    path('', ArticleListView.as_view(), name='articles'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='view'),

]


urlpatterns = [
    path('articles/', include(article_urls)),
]