from django.views import generic

from articles.models import Article


class IndexView(generic.ListView):
    template_name = 'articles/index.html'

    def get_queryset(self):
        return Article.objects.all()[:5]
