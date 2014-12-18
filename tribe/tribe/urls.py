from django.conf.urls import patterns, include, url
from rest_framework import routers
from tribe import views

from django.contrib import admin

from django.contrib.auth.views import login, logout

admin.autodiscover()

# change title for admin site
admin.site.site_header = 'Tribe'

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tribe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^accounts/register$', views.register, name='register'),
    url(r'^accounts/login/$', login),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^mytribe/$', views.mytribe),
    url(r'^admin/', include(admin.site.urls)),

    # API
    url(r'^api/v0.1/', include(router.urls)),
    url(r'^api/v0.1/users/register',views.create_auth),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
