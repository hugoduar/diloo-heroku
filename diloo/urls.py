from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'diloo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','dilooapp.views.home'),
    url(r'^category/(?P<id_category>\d+)$', 'dilooapp.views.category'),
    url(r'^login/$', 'dilooapp.views.index', name="login"),
    url(r'^login/enter$', 'dilooapp.views.login'),
    url(r'^login/logout$', 'dilooapp.views.logout'),
    url(r'^login/(?P<numero>\d+)$', 'dilooapp.views.show'),
)
