from django.conf.urls import patterns, include, url
from tribe import views

from django.contrib import admin
admin.autodiscover()

# change title for admin site
admin.site.site_header = 'Tribe'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tribe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^main/', include('main.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
