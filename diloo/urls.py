from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'diloo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','app.views.main', name="main"),
    url(r'^feed$','app.views.feed', name="feed"),
    url(r'^login$', 'app.views.login', name="login"),
    url(r'^register$', 'app.views.register', name="register"),
    url(r'^logout$', 'app.views.logout', name="logout"),
)

