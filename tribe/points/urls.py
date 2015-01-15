from django.conf.urls import patterns, include, url
from django.contrib import admin
from points import views

admin.autodiscover()

urlpatterns = patterns('',

    url(r'/?^$', views.TaskTemplateList.as_view(), name='task-list'),

    url(r'^new/$',
        views.TaskTemplateCreate.as_view(success_url="/mytribe/tasks/"),
        name='tasktemplate_create'),

    url(r'^(?P<pk>\d+)/$', views.TaskTemplateDetail.as_view(), name='tasktemplate-detail'),

    url(r'^(?P<pk>\d+)/update/$', views.TaskTemplateUpdate.as_view()),
)
