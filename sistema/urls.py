from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_header = 'CAAFI'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sistema.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'caafi.views.index', name='index'),
    url(r'^catalogo/(?P<language_name>\w+)/$', 'caafi.views.catalog', name='catalogo'),
    url(r'^catalogo/(?P<language_name>\w+)/(?P<category_name>\w+)$', 'caafi.views.catalog_categories', name='lista_categorias'),
    url(r'^catalogo/(?P<language_name>\w+)/(?P<category_name>\w+)/(?P<subcategory_name>\w+)$', 'caafi.views.catalog_subcategories', name='lista_subcategorias'),
    url(r'^busqueda/$', 'caafi.views.search', name='busqueda'),
)
