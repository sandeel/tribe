from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView
from tribe.serializers import UserSerializer
from rest_framework import permissions
from rest_framework.decorators import detail_route
from django.contrib.auth import get_user_model
from tribe.forms import RegistrationForm
from rest_framework import status

def index(request):
    return render(request, 'tribe/landing_page.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
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

@api_view(['POST'])
@permission_classes([AllowAny])
def api_register(request):
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

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAdminUser,)
