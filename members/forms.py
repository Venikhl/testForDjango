from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Form for creating an extended version of a build in user model.
class NewUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
