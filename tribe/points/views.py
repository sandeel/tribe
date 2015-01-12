from django.shortcuts import render
from django.views.generic.list import ListView
from points.models import TaskTemplate

class TaskTemplateListView(ListView):

    model = TaskTemplate

    def get_queryset(self):
        if (not self.request.user.tribe):
            return TaskTemplate.objects.none()

        return TaskTemplate.objects.filter(tribe=self.request.user.tribe)
