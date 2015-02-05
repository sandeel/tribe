from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from tribe.serializers import UserSerializer
from tribe.serializers import TribeSerializer
from tribe.serializers import InvitedUserSerializer
from rest_framework import permissions
from rest_framework.decorators import detail_route
from django.contrib.auth import get_user_model
from tribe.forms import RegistrationForm
from tribe.forms import CreateTribeForm
from tribe.forms import InvitedUserForm
from rest_framework import status
from tribe.models import Tribe
from tribe.models import TribeUser
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404
from rest_framework import filters
from tribe.permissions import IsAuthenticatedOrPost
from tribe.models import InvitedUser
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.shortcuts import redirect

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/mytribe")
    else:
        form = RegistrationForm()
    return render(request, "tribe/index.html", {
        'form': form,
    })

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, new_user)
            return HttpResponseRedirect("/create_tribe/")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

def create_tribe(request):
    if request.method == 'POST':
        form = CreateTribeForm(request.POST)
        if form.is_valid():
            new_tribe = form.save()
            new_tribe.members.add(request.user)
            new_tribe.leaders.add(request.user)
            new_tribe.save()
            return HttpResponseRedirect("/mytribe")
    else:
        form = CreateTribeForm()
    return render(request, "tribe/create_tribe.html", {
        'form': form,
    })

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

@login_required
def mytribe(request):
    return render(request, 'tribe/my_tribe.html')

class TribeUpdate(UpdateView):
    model = Tribe
    fields = ['name']
    template_name_suffix = '_update_form'

    def get_object(self):
        return get_object_or_404(Tribe, pk=self.request.user.tribe.id)

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['invited_users'] = InvitedUser.objects.all()
        context['invite_form'] = InvitedUserForm()
        return context

class TribeUserDetailView(DetailView):

    def get_queryset(self):
        return TribeUser.objects.filter(pk__in=self.request.user.tribe.members.values_list('id',flat=True))


class InvitedUserList(CreateView):
    model = InvitedUser
    fields = ['email']
    template_name = "tribe/inviteduser_list.html"
    form_class = InvitedUserForm

    def get_context_data(self, **kwargs):
        context = super(InvitedUserList, self).get_context_data(**kwargs)
        context['invitees'] = self.request.user.tribe.invited_users.all()
        return context

    def form_valid(self, form):

        InvitedUserViewSet.as_view({'post': 'create',})(self.request)
        return redirect('/invite_tribe_members/')

"""
API Views
"""
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tribes': reverse('tribe-list', request=request, format=format),
        })

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrPost,]

    def create(self, request):
        VALID_USER_FIELDS = [f.name for f in get_user_model()._meta.fields]
        DEFAULTS = {
            # you can define any defaults that you would like for the user, here
        }
        serialized = UserSerializer(data=request.DATA)
        if serialized.is_valid():
            user_data = {field: data for (field, data) in request.DATA.items() if field in VALID_USER_FIELDS}
            user_data.update(DEFAULTS)
            user = get_user_model().objects.create(
                **user_data
            )
            return Response(UserSerializer(instance=user).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return TribeUser.objects.all()
        else:
            return TribeUser.objects.filter(id = self.request.user.id)

class TribeViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = Tribe.objects.all()
    serializer_class = TribeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serialized = TribeSerializer(data = request.data)
        VALID__FIELDS = [f.name for f in Tribe._meta.fields]
        if serialized.is_valid():
            tribe_data = {field: data for (field, data) in request.DATA.items() if field in VALID__FIELDS}
            tribe = Tribe.objects.create(
                **tribe_data
            )
            tribe.members.add(request.user)
            tribe.leaders.add(request.user)
            tribe.save()
            return Response(TribeSerializer(instance=tribe, context={'request': request}).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tribe.objects.all()
        elif self.request.user.tribe == None:
            return Tribe.objects.none()
        else:
            return Tribe.objects.filter(pk=self.request.user.tribe.id)

class InvitedUserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = InvitedUser.objects.all()
    serializer_class = InvitedUserSerializer
