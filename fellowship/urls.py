from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tumblelog.views.home', name='home'),
    # url(r'^tumblelog/', include('tumblelog.foo.urls')),
    #----------------------
    # Apps urls call
    #----------------------
    url(r'^$',  include('homepage.urls')),
    url(r'^home/',  include('homepage.urls')),
    url(r'^bubbles/',  include('bubbles.urls')),

    #----------------------
    # Admin url
    #----------------------
    url(r'^mongonaut/', include('mongonaut.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)

# -----------------------------------------------------------
# Load various media files on django debugging server
# -----------------------------------------------------------
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + '/css'}),
        (r'^img/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + '/img'}),
        (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + '/js'}),
        #(r'^files/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + '/files'}),
    )

