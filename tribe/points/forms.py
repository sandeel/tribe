from django import forms
from points.models import CheckIn
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout
from crispy_forms.layout import Hidden

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
        fields = []
