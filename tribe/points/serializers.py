from rest_framework import serializers
from points.models import Category
from points.models import Task
from points.models import TribeUser
from points.models import CheckIn

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class CheckInSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckIn
        fields = ('id', 'task', 'date', 'time')


class TaskSerializer(serializers.ModelSerializer):


    def create(self, validated_data):
        task = Task.objects.create(
                               name = validated_data['name'],
                               description = validated_data['description'],
                               tribe = self.context['request'].user.tribe,
                               category = validated_data['category'],
                               points_reward = validated_data['points_reward'],
        )

        print(task.category)
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
