from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    url(r'^$', 'status.views.index', name='status'),
)

urlpatterns += staticfiles_urlpatterns()
