from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


@apphook_pool.register
class ArticlesApphook(CMSApp):
    app_name = "articles"
    name = _("Articles Application")

    def get_urls(self, page=None, language=None, **kwargs):
        return ["articles.urls"]
