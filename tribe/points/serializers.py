from rest_framework import serializers
from points.models import Category
from points.models import Task
from points.models import TribeUser
from points.models import CheckIn
import datetime

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class CheckInSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        checkin = CheckIn.objects.create(
                               user = self.context['request'].user,
                               task = validated_data['task'],
                               date = datetime.datetime.today(),
                               points_awarded = validated_data['task'].points_reward
        )


        return checkin

    class Meta:
        model = CheckIn
        fields = ('id', 'user', 'task', 'date', 'points_awarded')
        extra_kwargs = {'user': {'read_only': True},
                        'date': {'read_only': True},
                        'points_awarded': {'read_only': True}
        }


class TaskSerializer(serializers.ModelSerializer):


    def create(self, validated_data):
        task = Task.objects.create(
                               name = validated_data['name'],
                               description = validated_data['description'],
                               tribe = self.context['request'].user.tribe,
                               category = validated_data['category'],
                               points_reward = validated_data['points_reward'],
        )

        task.assigned_users = validated_data['assigned_users']

        return task

    class Meta:
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
