from django.conf.urls.defaults import *
from django.conf import settings

from core.views import PostListView, PostCreateView, TagListView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = patterns('homepage.views',
    #url(r'^$',             'home',      name="home"),
    url(r'^$', PostListView.as_view(),      name="post-list"),
	url(r'^add/$', PostCreateView.as_view(), name='post-create'),
	url(r'^tags/$', TagListView.as_view(), name='tag-list'),
	url(r'^(?P<pk>[\w\d]+)/$', PostDetailView.as_view(), name='post-detail'),
	url(r'^(?P<pk>[\w\d]+)/edit/$', PostUpdateView.as_view(), name='post-update'),
	url(r'^(?P<pk>[\w\d]+)/delete/$', PostDeleteView.as_view(), name='post-delete'),

)
