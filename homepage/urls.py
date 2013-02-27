from django.conf.urls.defaults import *
from django.conf import settings

from core.views import PostListView

urlpatterns = patterns('homepage.views',
    #url(r'^$',             'home',      name="home"),
    url(r'^$',             PostListView.as_view(),      name="post-list"),
)
