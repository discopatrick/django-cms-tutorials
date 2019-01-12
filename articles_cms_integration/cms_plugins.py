from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from articles_cms_integration.models import ArticlePluginModel
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin
class ArticlePluginPublisher(CMSPluginBase):
    model = ArticlePluginModel
    module = _("Articles")
    name = _("Article Plugin")
    render_template = "articles_cms_integration/article_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
