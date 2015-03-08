from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_header = 'CAAFI'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sistema.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'caafi.views.index', name='index'),
    url(r'^catalogo/(?P<language_id>\d+)/$', 'caafi.views.catalog', name='catalogo'),
    url(r'^lista/$', 'caafi.views.url_list', name='lista'),
    url(r'^busqueda/$', 'caafi.views.search', name='busqueda'),
)
