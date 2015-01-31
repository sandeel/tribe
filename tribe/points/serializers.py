from rest_framework import serializers
from points.models import Category
from points.models import Task
from points.models import TribeUser
from points.models import CheckIn
from points.models import Approval
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

class ApprovalSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        approval = Approval.objects.create(
                               approver = self.context['request'].user,
                               checkin = validated_data['checkin'],
        )


        return approval

    class Meta:
        model = Approval
        fields = ('id', 'checkin')

class FormToSerializerBooleanField(serializers.BooleanField):
    ''' workaround to convert django form field to serializer form field
    see the issue https://github.com/tomchristie/django-rest-framework/issues/2394
    '''
    TRUE_VALUES = set(('t', 'T', 'true', 'True', 'TRUE', '1', 1, True,'On','on','ON'))
    FALSE_VALUES = set(('f', 'F', 'false', 'False', 'FALSE', '0', 0, 0.0, False,'Off','off','OFF'))


class TaskSerializer(serializers.ModelSerializer):

    monday = FormToSerializerBooleanField()
    tuesday = FormToSerializerBooleanField()
    wednesday = FormToSerializerBooleanField()
    thursday = FormToSerializerBooleanField()
    friday = FormToSerializerBooleanField()
    saturday = FormToSerializerBooleanField()
    sunday = FormToSerializerBooleanField()

    def create(self, validated_data):
        task = Task.objects.create(
                               name = validated_data['name'],
                               description = validated_data['description'],
                               tribe = self.context['request'].user.tribe,
                               category = validated_data['category'],
                               points_reward = validated_data['points_reward'],

                               monday = validated_data['monday'],
                               tuesday = validated_data['tuesday'],
                               wednesday = validated_data['wednesday'],
                               thursday = validated_data['thursday'],
                               friday = validated_data['friday'],
                               saturday = validated_data['saturday'],
                               sunday = validated_data['sunday'],
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
