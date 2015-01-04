from rest_framework import serializers
from django.contrib.auth import get_user_model
from tribe.models import Tribe
from tribe.models import TribeUser
from tribe.models import InvitedUser

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'is_leader')
        extra_kwargs = {'password': {'write_only': True}}

class TribeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tribe
        fields = ('id', 'name', 'invited_users', 'members', 'leaders')

class InvitedUserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = InvitedUser
        fields = ('id', 'email', 'tribe')

