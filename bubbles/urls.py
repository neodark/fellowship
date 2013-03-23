from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('bubbles.views',
    url(r'^$',  'bubbles',  name="bubbles"),
)
