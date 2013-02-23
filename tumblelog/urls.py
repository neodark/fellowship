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


    #----------------------
    # Admin url
    #----------------------
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
)
