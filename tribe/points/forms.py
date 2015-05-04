from django import forms
from points.models import CheckIn
from points.models import Task
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Hidden
from crispy_forms.layout import Field
from crispy_forms.layout import Layout, Fieldset, MultiField, ButtonHolder, Submit

class CheckInForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout = Layout(
            Hidden('task','{{ object.id }}')
        )

        self.helper.add_input(Submit('checkin', 'Check In'))
        super(CheckInForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CheckIn
        fields = ['image']

class ApprovalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ApprovalForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.layout.append(
            Hidden('checkin','{{ object.id }}')
        )

        self.helper.add_input(Submit('approve', 'Approve'))


    class Meta:
        model = CheckIn

class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()

        self.helper.layout = Layout(
            Fieldset(
                'create a new task',
                'name',
                'description',
                'category',
                'points_reward',
                Fieldset(
                    'Tribe members available to',
                    'assigned_users',
                ),
                Fieldset(
                    'When available',
                    'Days available',
                    'monday',
                    'tuesday',
                    'wednesday',
                    'thursday',
                    'friday',
                    'saturday',
                    'sunday',
                    'time_available_from',
                    'time_available_to',
                    'date_available',
                    'date_available_to',
                ),
            ),
            ButtonHolder(
                Submit('submit', 'Submit'),
            )
        )

        self.helper['time_available_from'].wrap(Field, placeholder="00:00:00")
        self.helper['time_available_to'].wrap(Field, placeholder="00:00:00")
        self.helper['date_available'].wrap(Field, placeholder="YYYY-MM-DD")

        super(TaskForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'category',
                  'points_reward', 'assigned_users',
                  'date_available',
                  'date_available_to',
                  'time_available_from',
                  'time_available_to',
                  'monday',
                  'tuesday',
                  'wednesday',
                  'thursday',
                  'friday',
                  'saturday',
                  'sunday')

