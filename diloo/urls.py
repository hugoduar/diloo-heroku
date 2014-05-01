from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'diloo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^base$', 'dilooapp.views.base'),
    url(r'^$','dilooapp.views.home'),
    url(r'^category/(?P<id_category>\d+)$', 'dilooapp.views.category'),
    url(r'^register$', 'dilooapp.views.register', name="register"),
    url(r'^login$', 'dilooapp.views.login', name="login"),
    #url(r'^login/enter$', 'dilooapp.views.login'),
    url(r'^logout$', 'dilooapp.views.logout'),
    url(r'^login/(?P<numero>\d+)$', 'dilooapp.views.show'),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
    #     {'document_root': settings.MEDIA_ROOT})
)
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#018005002500

