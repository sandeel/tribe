from rest_framework import serializers
from django.contrib.auth import get_user_model
from tribe.models import Tribe
from tribe.models import TribeUser

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'is_leader')
        extra_kwargs = {'password': {'write_only': True}}

class TribeSerializer(serializers.HyperlinkedModelSerializer):

    members = serializers.PrimaryKeyRelatedField(many=True, queryset=TribeUser.objects.filter())

    leaders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Tribe
        fields = ('id', 'name', 'members', 'leaders')
