from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from points.models import Task
from points.models import Category
from points.models import CheckIn
from points.serializers import CategorySerializer
from points.serializers import TaskSerializer
from points.serializers import CheckInSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from points.forms import CheckInForm
from rest_framework import reverse

class TaskCreate(CreateView):
    model = Task

    fields = ('id', 'name', 'description', 'category',
              'points_reward', 'assigned_users',
              'date_available',
              'time_available_from',
              'time_available_to',
              'monday',
              'tuesday',
              'wednesday',
              'thursday',
              'friday',
              'saturday',
              'sunday')

    def form_valid(self, form):
        """
        If the form is **valid** send the data to the API
        and redirect to the tasks list
        """
        TaskViewSet.as_view({'post': 'create',})(self.request)
        return redirect('/mytribe/tasks')


class TaskDetail(DetailView, FormView):
    model = Task

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['form'] = CheckInForm() 
        return context

    def post(self, request, *args, **kwargs):

        CheckInViewSet.as_view({'post': 'create',})(self.request)
        return redirect('/mytribe/tasks/')

class TaskUpdate(UpdateView):
    model = Task

class TaskList(ListView):
    model = Task
    template_name = "points/task_list.html"


    def get_queryset(self):
        id = self.request.user.id
        tasks = Task.objects.filter(assigned_users__id=id)
        filtered_by_available = (x for x in tasks if x.available_now)
        return filtered_by_available


# Categories
class CategoryList(ListView):
    model = Category

class CategoryDetail(DetailView):
    model = Category

class CategoryCreate(CreateView):
    model = Category

    fields = [
                'name',
                'description',
             ]

    def form_valid(self, form):
        form.instance.tribe = self.request.user.tribe
        return super(CategoryCreate, self).form_valid(form)

## API views
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serialized = CategorySerializer(data = request.data)
        if serialized.is_valid():
            category = Category.objects.create(name = request.DATA.get('name'),
                                               tribe = request.user.tribe)
            category.tribe = request.user.tribe
            category.save()
                
            return Response(CategorySerializer(instance=category, context={'request': request}).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return self.request.user.tribe.categories.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        the_users_tribe_id = self.request.user.tribe.id
        return Task.objects.filter(tribe__id = the_users_tribe_id)


class CheckInViewSet(viewsets.ModelViewSet):
    serializer_class = CheckInSerializer
    permission_classes = [IsAuthenticated]
    queryset = CheckIn.objects.all()
