from django.conf.urls import patterns, include, url
from tribe import views

from django.contrib import admin

from django.contrib.auth.views import login, logout

admin.autodiscover()

# change title for admin site
admin.site.site_header = 'Tribe'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tribe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^accounts/login/$', login),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^mytribe/$', views.mytribe),
    url(r'^admin/', include(admin.site.urls)),
)
