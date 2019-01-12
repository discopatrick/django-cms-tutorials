from django.db import models
from cms.models import CMSPlugin
from articles.models import Article


class ArticlePluginModel(CMSPlugin):
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return self.article.title
