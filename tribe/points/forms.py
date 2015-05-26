from django import forms
from points.models import CheckIn
from tribe.models import TribeUser
from points.models import Task
from points.models import Reward
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Hidden
from crispy_forms.layout import Field
from crispy_forms.layout import Layout, Fieldset, MultiField, ButtonHolder, Submit, HTML, Div
from crispy_forms.bootstrap import InlineField

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

        self.helper.add_input(Submit('checkin', 'Complete!'))
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
                'task details',
                'name',
                'description',
                'category',
                'points_reward',
                HTML("""
                    <div class="panel panel-default">
                      <div class="panel-heading"><strong>Available every</strong></div>
                      <div class="panel-body">
                """),
                Div(
                    Div('monday',css_class='col-md-3',),
                    Div('tuesday',css_class='col-md-3',),
                    Div('wednesday',css_class='col-md-3',),
                    Div('thursday',css_class='col-md-3',),
                    css_class='row',
                ),
                Div(
                    Div('friday',css_class='col-md-3',),
                    Div('saturday',css_class='col-md-3',),
                    Div('sunday',css_class='col-md-3',),
                    css_class='row',
                ),
                HTML("""
                      </div>
                    </div>
                """),
            ),
            Fieldset(
                'Availability',
                HTML("""
                    <div class="alert alert-info" role="alert">
                      Leave this blank for tasks available to your whole tribe.
                    </div>
                """),
                'assigned_users',
            ),
            Fieldset(
                'Time',
                HTML("""
                    <div class="alert alert-info" role="alert">
                      Enter these if task can only be completed between certain times.
                    </div>
                """),
                'time_available_from',
                'time_available_to',
            ),
            Fieldset(
                'Date',
                HTML("""
                    <div class="alert alert-info" role="alert">
                      Only enter these if task is a once-off
                    </div>
                """),
                'date_available',
                'date_available_to',
            ),
            Fieldset(
                '',
                ButtonHolder(
                    Submit('submit', 'Submit',),
                ),
            )
        )

        self.helper['points_reward'].wrap(Field, placeholder="100")
        self.helper['time_available_from'].wrap(Field, placeholder="00:00:00")
        self.helper['time_available_to'].wrap(Field, placeholder="00:00:00")
        self.helper['date_available'].wrap(Field, placeholder="yyyy-mm-dd")
        self.helper['date_available_to'].wrap(Field, placeholder="yyyy-mm-dd")

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

class RewardForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()

        self.helper.add_input(Submit('submit', 'Submit'))


        super(RewardForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Reward
        fields = ('id', 'name', 'description','available_to',
                  'points_required')

