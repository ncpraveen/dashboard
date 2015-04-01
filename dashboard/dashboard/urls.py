from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    url(r'^board/', include('board.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
