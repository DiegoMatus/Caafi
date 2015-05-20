from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_header = 'CAAFI'
urlpatterns = patterns('caafi.views',

    url(r'^$', 'index'),
    url(r'^(?P<language_name>\w+)/$', 'lista_categorias'),
    url(r'^(?P<language_name>\w+)/(?P<category_name>[\w|\W]+)/$', 'lista_subcategorias'),
    url(r'^(?P<language_name>\w+)/(?P<category_name>[\w|\W]+)/(?P<subcategory_name>\w+)$', 'lista_urls'),
)