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



    # Task Templates
    url(r'task_templates/$', views.TaskTemplateList.as_view(), name='tasktemplate-list'),

    url(r'task_templates/new$',
        views.TaskTemplateCreate.as_view(success_url="/mytribe/tasks/task_templates/"),
        name='tasktemplate-create'),

    url(r'task_templates/(?P<pk>\d+)$', views.TaskTemplateDetail.as_view(), name='tasktemplate-detail'),

    url(r'task_templates/(?P<pk>\d+)/update/$',
        views.TaskTemplateUpdate.as_view(success_url="/mytribe/tasks/task_templates")
       ),





    url(r'^(?P<pk>\d+)/$',
        views.TaskUpdate.as_view(success_url="/mytribe/tasks"),
        name='task-detail'),

    url(r'/?^$', views.TaskList.as_view(), name='task-list'),

)
