from django.conf.urls import *
from django.conf import settings

urlpatterns = patterns('bubbles.views',
    url(r'^$',  'bubbles',  name="bubbles"),
)
