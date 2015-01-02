from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from tribe import views

from django.contrib import admin

from django.contrib.auth.views import login, logout

from django.conf.urls import include

admin.autodiscover()

# change title for admin site
admin.site.site_header = 'Tribe'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tribes', views.TribeViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tribe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', views.index, name='index'),
    url(r'^accounts/register$', views.register, name='register'),
    url(r'^accounts/login/$', login),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^mytribe/$', views.mytribe),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
)
