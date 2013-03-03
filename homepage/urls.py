from django.conf.urls.defaults import *
from django.conf import settings

from core.views import PostListView, PostCreateView, TagListView

urlpatterns = patterns('homepage.views',
    #url(r'^$',             'home',      name="home"),
    url(r'^$', PostListView.as_view(),      name="post-list"),
	url(r'^add/$', PostCreateView.as_view(), name='post-create'),
	url(r'^tags/$', TagListView.as_view(), name='tag-list'),
)
