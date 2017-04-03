from django.conf.urls import patterns, include, url
from django.contrib import admin
from cms_put import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.showAll, name='mostrar todo'),
    url(r'^(.+)', views.processRequest, name='procesar la peticion recibida'),
    url(r'^admin/', include(admin.site.urls)),
)
