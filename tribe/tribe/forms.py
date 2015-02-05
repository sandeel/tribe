from django import forms
from django.contrib.auth import get_user_model
from tribe.models import Tribe
from tribe.models import InvitedUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'register'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(RegistrationForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget=forms.widgets.TextInput,label="Email")
    password1 = forms.CharField(widget=forms.widgets.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.widgets.PasswordInput,
                                label="Confirm Password")

    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(RegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class CreateTribeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'create_tribe'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(CreateTribeForm, self).__init__(*args, **kwargs)

        name = forms.CharField(widget=forms.widgets.TextInput,label="Name")

    class Meta:
        model = Tribe
        fields = ['name',]

class InvitedUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InvitedUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))

        email = forms.CharField(widget=forms.widgets.TextInput,label="Email address")

    class Meta:
        model = InvitedUser
        fields = ['email',]
