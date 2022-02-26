from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Person, Identy, Jharsewa, Education
class DateInput(forms.DateInput):
    input_type = 'date'


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = "__all__"
        widgets = {
            'year_of_pass': DateInput(),
        }


class JharsewaForm(forms.ModelForm):
    class Meta:
        model = Jharsewa
        fields = "__all__"
        widgets = {
            'date_of_issue': DateInput(),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Create a UserUpdateForm to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

# Create a ProfileUpdateForm to update image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

# Create a IdentyUpdateForm to update image
class IdentyUpdateForm(forms.ModelForm):
    class Meta:
        model = Identy
        fields = "__all__"
