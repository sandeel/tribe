from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from points.models import Task
from points.models import Category
from points.serializers import CategorySerializer
from points.serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class TaskCreate(CreateView):
    model = Task
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
        return super(TaskCreate, self).form_valid(form)

class TaskDetail(DetailView):
    model = Task

class TaskUpdate(UpdateView):
    model = Task

class TaskList(ListView):
    model = Task

    def get_queryset(self):
        id = self.request.user.id
        return Task.objects.filter(assigned_users__id=id)


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
    queryset = Category.objects.all()
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
        the_users_tribe_id = self.request.user.tribe.id
        return Category.objects.filter(tribe__id = the_users_tribe_id)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


    def create(self, request):
        serialized = TaslSerializer(data = request.data)
        if serialized.is_valid():
            task = Task.objects.create(name = request.DATA.get('name'),
                                               tribe = request.user.tribe)
            task.tribe = request.user.tribe
            task.save()
                
            return Response(TaskSerializer(instance=task, context={'request': request}).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        the_users_tribe_id = self.request.user.tribe.id
        return Task.objects.filter(tribe__id = the_users_tribe_id)
