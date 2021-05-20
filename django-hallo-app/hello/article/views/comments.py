from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import CreateView
from django.shortcuts import reverse, get_object_or_404

from article.forms import CommentForm
from article.models import Comment, Article


class ArticleCommentCreate(PermissionRequiredMixin, CreateView):
    template_name = 'comments/create.html'
    form_class = CommentForm
    model = Comment
    permission_required = 'article.add_comment'

    def get_success_url(self):
        return reverse(
            'article:view',
            kwargs={'pk': self.kwargs.get('pk')}
        )
    
    def form_valid(self, form):
        article = get_object_or_404(Article, id=self.kwargs.get('pk'))

        comment = form.instance
        comment.article = article
        comment.author = self.request.user

        return super().form_valid(form)
