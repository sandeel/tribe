from rest_framework import serializers
from django.contrib.auth import get_user_model
from tribe.models import Tribe

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class TribeSerializer(serializers.HyperlinkedModelSerializer):

    tribeuser_set = serializers.HyperlinkedRelatedField(many=True, view_name='tribeuser-detail', read_only=True)

    class Meta:
        model = Tribe
        fields = ('id', 'name', 'tribeuser_set')
