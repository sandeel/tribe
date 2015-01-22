from rest_framework import serializers
from points.models import Category
from points.models import Task

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')



class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'tribe', 'name', 'description', 'category', 'recurring_strategy',
                  'points_reward', 'assigned_users')
