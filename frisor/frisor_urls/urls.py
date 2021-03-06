from django.conf.urls import url

import tagulous.views
from .models import Tags
from .views import UrlView, AddUrlView


urlpatterns = [
    url(r'^tags/autocomplete/', tagulous.views.autocomplete,
        {'tag_model': Tags}, name='url_tags_autocomplete'),
    url(r'^$', UrlView.as_view()),
    url(r'^add_url', AddUrlView.as_view())
]
