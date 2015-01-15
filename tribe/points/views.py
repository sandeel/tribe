from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from points.models import TaskTemplate

class TaskTemplateCreate(CreateView):
    model = TaskTemplate
    fields = ['name', 'category', 'description']

    def form_valid(self, form):
        form.instance.tribe = self.request.user.tribe
        return super(TaskTemplateCreate, self).form_valid(form)

class TaskTemplateDetail(DetailView):
    model = TaskTemplate

class TaskTemplateList(ListView):

    model = TaskTemplate

    def get_queryset(self):
        if (not self.request.user.tribe):
            return TaskTemplate.objects.none()

        return TaskTemplate.objects.filter(tribe=self.request.user.tribe)

class TaskTemplateUpdate(UpdateView):
    model = TaskTemplate
    fields = ['name', 'category', 'description']
