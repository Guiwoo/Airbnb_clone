from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))

        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = (
            "email",
            "first_name",
            "last_name",
        )

    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        username = self.cleaned_data.get("email")
        user.username = username
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user

    # When you are usign forms.ModelForm
    # class Meta:
    #     model = models.User
    #     fields = ("first_name", "last_name", "email")

    # password = forms.CharField(widget=forms.PasswordInput)
    # password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    # def clean_password1(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password = self.cleaned_data.get("password")

    #     if password != password1:
    #         raise forms.ValidationError("Passwrod confirmation does not match")
    #     else:
    #         return password

    # def save(self, *args, **kwargs):
    #     # commit=False means Do not upload on database
    #     user = super().save(commit=False)
    #     username = self.cleaned_data.get("email")
    #     password = self.cleaned_data.get("password")
    #     user.username = username
    #     user.set_password(password)
    #     user.save()
