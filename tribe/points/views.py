from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from points.models import Task
from points.models import Category
from points.models import CheckIn
from points.models import Approval
from tribe.models import TribeUser
from points.models import Reward
from points.serializers import CategorySerializer
from points.serializers import TaskSerializer
from points.serializers import CheckInSerializer
from points.serializers import ApprovalSerializer
from points.serializers import RewardSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import redirect
from points.forms import CheckInForm
from points.forms import ApprovalForm
from rest_framework import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render

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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        """
        If the form is **valid** send the data to the API
        and redirect to the tasks list
        """
        TaskViewSet.as_view({'post': 'create',})(self.request)
        return redirect('/mytribe/tasks/')

    def get_context_data(self, **kwargs):
            context = super(TaskCreate, self).get_context_data(**kwargs)
            context['form'].fields['assigned_users'].queryset = TribeUser.objects.filter(tribe=self.request.user.tribe)
            return context


class TaskDetail(DetailView, FormView):
    model = Task
    permission_classes = [IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['form'] = CheckInForm() 
        return context

    def post(self, request, *args, **kwargs):

        CheckInViewSet.as_view({'post': 'create',})(self.request)
        return redirect('/mytribe/tasks/')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskDetail, self).dispatch(*args, **kwargs)

class TaskUpdate(UpdateView):
    model = Task

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskUpdate, self).dispatch(*args, **kwargs)

class TaskList(ListView):
    model = Task
    template_name = "points/task_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TaskList, self).dispatch(*args, **kwargs)


    def get_queryset(self):
        id = self.request.user.id
        tasks = Task.objects.filter(assigned_users__id=id)
        return tasks
        # filtered_by_available = (x for x in tasks if x.available_now)
        # return filtered_by_available


# Categories
class CategoryList(ListView):
    model = Category

    """
    Prevent unauthorized access
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryList, self).dispatch(*args, **kwargs)

class CategoryDetail(DetailView):
    model = Category

    """
    Prevent unauthorized access
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryDetail, self).dispatch(*args, **kwargs)

class CategoryCreate(CreateView):
    model = Category

    fields = [
                'name',
                'description',
             ]

    def form_valid(self, form):
        form.instance.tribe = self.request.user.tribe
        return super(CategoryCreate, self).form_valid(form)

    """
    Prevent unauthorized access
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryCreate, self).dispatch(*args, **kwargs)



class CategoryUpdate(UpdateView):
    model = Category
    template_name = "points/category_update.html"
    
    fields = [
                'name',
                'description',
             ]

    """
    Prevent unauthorized access
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CategoryUpdate, self).dispatch(*args, **kwargs)



# Rewards
class RewardCreate(CreateView):
    model = Reward

    fields = [
                'name',
                'description',
                'available_to',
                'points_required',
             ]

    def post(self, request, *args, **kwargs):

        RewardViewSet.as_view({'post': 'create',})(self.request)
        return redirect('/mytribe/tasks/rewards/')

class RewardList(ListView):
    model = Reward

    def get_queryset(self):
        return self.request.user.tribe.rewards.all()

class RewardDetail(DetailView):
    model = Reward

class RewardUpdate(UpdateView):
    model = Reward

    fields = [
                'name',
                'description',
                'available_to',
                'points_required',
             ]


# CheckIns
class CheckInDetail(DetailView):
    model = CheckIn
    
    def post(self, form, *args, **kwargs):
        ApprovalViewSet.as_view({'post': 'create',})(self.request)
        return redirect('/mytribe/tasks/')

class CheckInList(ListView):
    model = CheckIn

    def get_queryset(self):
        return Task.objects.get(id = self.kwargs['pk']).checkins.all()




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

class ApprovalViewSet(viewsets.ModelViewSet):
    serializer_class = ApprovalSerializer
    permission_classes = [IsAuthenticated]
    queryset = Approval.objects.all()

class RewardViewSet(viewsets.ModelViewSet):
    serializer_class = RewardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.tribe.rewards.all()


class PointsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "points/points.html", { 
            'rewards' : Reward.objects.filter(tribe=self.request.user.tribe)
                    })

    """
    Prevent unauthorized access
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PointsView, self).dispatch(*args, **kwargs)
