from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from tribe import views
from tribe.models import TribeUser
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls import include
import points
from points.views import CategoryViewSet
from points.views import TaskViewSet
from points.views import CheckInViewSet
from points.views import ApprovalViewSet
from points.views import RewardViewSet

admin.autodiscover()

# change title for admin site
admin.site.site_header = 'Tribe'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tribes', views.TribeViewSet)
router.register(r'invited_users', views.InvitedUserViewSet)
router.register(r'categories', CategoryViewSet, base_name='category')
router.register(r'tasks', TaskViewSet, base_name='task')
router.register(r'checkins', CheckInViewSet)
router.register(r'approvals', ApprovalViewSet)
router.register(r'rewards', RewardViewSet, base_name='reward')

urlpatterns = patterns('',
    url(r'/?^$', views.index, name='index'),

    url(r'^create_tribe/$', views.create_tribe, name='create_tribe'),
    url(r'^mytribe/invite_tribe_members/$', views.InvitedUserList.as_view(), name='invite_tribe_members'),

    url(r'^mytribe/tasks/', include('points.urls')),

    # tribe members
    url(r'^mytribe/(?P<pk>\d+)/$', views.TribeUserDetailView.as_view(), name='tribemembers'),
    url(r'mytribe/(?P<pk>\d+)/update/$',
        views.TribeUserUpdate.as_view(success_url="/mytribe/%(id)s/")
       ),

    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/login/$', login),
    url(r'^logout/$', logout, {'next_page': '/'}),

    url(r'^mytribe/$', views.mytribe),
    url(r'^mytribe/update/$', views.TribeUpdate.as_view(success_url='/mytribe/')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls',
                                namespace='rest_framework')),
)
