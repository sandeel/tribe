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
from rest_framework import permissions
from rest_framework.decorators import detail_route
from django.contrib.auth import get_user_model
from tribe.forms import RegistrationForm
from rest_framework import status
from tribe.models import Tribe
from tribe.models import TribeUser

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
            return HttpResponseRedirect("/mytribe")
    else:
        form = RegistrationForm()
    return render(request, "registration/register.html", {
        'form': form,
    })

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

def mytribe(request):
    return render(request, 'tribe/logged_in.html')



"""
API
"""
@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        })

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request):
        VALID_USER_FIELDS = [f.name for f in get_user_model()._meta.fields]
        DEFAULTS = {
            # you can define any defaults that you would like for the user, here
        }
        serialized = UserSerializer(data=request.DATA)
        if serialized.is_valid():
            user_data = {field: data for (field, data) in request.DATA.items() if field in VALID_USER_FIELDS}
            user_data.update(DEFAULTS)
            user = get_user_model().objects.create_user(
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
            tribe.tribeuser_set.add(request.user)
            tribe.save()
            print(tribe.tribeuser_set.all())
            return Response(TribeSerializer(instance=tribe, context={'request': request}).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tribe.objects.all()
        elif self.request.user.tribe == None:
            return Tribe.objects.none()
        else:
            return Tribe.objects.filter(id = self.request.user.tribe.id)
