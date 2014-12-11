from django.conf.urls import patterns, include, url

from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^submit/$','testapp.views.indexall'),
    url(r'^search_form/$','testapp.views.show'),
    url(r'^search/$','testapp.views.search'),
    url(r'^title/$','testapp.views.title'),
    url(r'^allpage/$','testapp.views.listpage'),
)
