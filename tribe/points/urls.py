from django.conf.urls import patterns, include, url
from django.contrib import admin
from points import views

admin.autodiscover()

urlpatterns = patterns('',

    # Categories
    url(r'categories/$', views.CategoryList.as_view(), name='category-list'),

    url(r'categories/(?P<pk>\d+)$',
        views.CategoryDetail.as_view(),
        name='category-detail'),

    url(r'categories/new$',
        views.CategoryCreate.as_view(success_url="/mytribe/tasks/categories/"),
        name='category-create'),



    # Tasks
    url(r'/?^$', views.TaskList.as_view(), name='task-list'),

    url(r'new/$',
        views.TaskCreate.as_view(success_url="/mytribe/tasks/"),
        name='tasks-create'),

    url(r'(?P<pk>\d+)/$', views.TaskDetail.as_view(), name='task-detail'),

    url(r'(?P<pk>\d+)/update/$',
        views.TaskUpdate.as_view(success_url="/mytribe/tasks/%(id)s/")
       ),
)
