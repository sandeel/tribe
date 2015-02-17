from django.conf.urls import patterns, include, url
from django.contrib import admin
from points import views
from points.models import CheckIn

admin.autodiscover()

urlpatterns = patterns('',

    url(r'points/$', views.PointsView.as_view(), name='points'),

    # Categories
    url(r'categories/$', views.CategoryList.as_view(), name='category-list'),

    url(r'categories/(?P<pk>\d+)/$',
        views.CategoryDetail.as_view(),
        name='category-detail'),

    url(r'categories/new/$',
        views.CategoryCreate.as_view(success_url="/mytribe/tasks/categories/"),
        name='category-create'),

    url(r'categories/(?P<pk>\d+)/update/$',
        views.CategoryUpdate.as_view(success_url="/mytribe/tasks/categories/%(id)s/")
       ),
    
    url(r'checkins/(?P<pk>\d+)/$',
        views.CheckInDetail.as_view()
       ),


    url(r'(?P<pk>\d+)/checkins/$',
        views.CheckInList.as_view()
       ),


    # Tasks
    url(r'/?^$', views.TaskList.as_view(), name='task-list'),

    url(r'new/$',
        views.TaskCreate.as_view(),
        name='task-create'),

    url(r'(?P<pk>\d+)/$', views.TaskDetail.as_view(), name='task-detail'),

    url(r'(?P<pk>\d+)/update/$',
        views.TaskUpdate.as_view(success_url="/mytribe/tasks/%(id)s/")
       ),


)
