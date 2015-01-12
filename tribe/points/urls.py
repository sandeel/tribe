from django.conf.urls import patterns, include, url
from points.views import TaskTemplateListView

urlpatterns = patterns('',

    url(r'^$', TaskTemplateListView.as_view(), name='task-list'),
)
