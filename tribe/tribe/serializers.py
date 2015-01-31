from rest_framework import serializers
from django.contrib.auth import get_user_model
from tribe.models import Tribe
from tribe.models import TribeUser
from tribe.models import InvitedUser

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password', 'is_leader')
        extra_kwargs = {'password': {'write_only': True}}

class TribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tribe
        fields = ('id', 'name', 'members', 'leaders')
        extra_kwargs = {'members': {'read_only': True}}
        extra_kwargs = {'leaders': {'read_only': True}}

    def create(self, validated_data):
        tribe = Tribe.objects.create(
                               members = [self.context['request'].user,],
                               leaders = [self.context['request'].user,],
                               name = validated_data['name'],
        )

        return tribe

class InvitedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvitedUser
        fields = ('id', 'email', 'tribe')

