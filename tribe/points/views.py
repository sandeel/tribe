from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from points.models import TaskTemplate
from points.models import Task

class TaskTemplateCreate(CreateView):
    model = TaskTemplate
    fields = [
                'name',
                'category',
                'description',
                'points_reward',
                'assigned_users',
                'recurring_strategy',
             ]

    def form_valid(self, form):
        form.instance.tribe = self.request.user.tribe
        return super(TaskTemplateCreate, self).form_valid(form)

class TaskTemplateDetail(DetailView):
    model = TaskTemplate

class TaskTemplateList(ListView):
    model = TaskTemplate

class TaskTemplateUpdate(UpdateView):
    model = TaskTemplate

class TaskUpdate(UpdateView):
    model = Task
    fields = ['marked_done']

class TaskList(ListView):
    model = Task

    def get_queryset(self):
        id = self.request.user.id
        return Task.objects.filter(task_template__assigned_users__id=id)



