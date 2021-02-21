from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length= 50, label = "Username")
    password = forms.CharField(max_length = 50, label = "Password",widget = forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label = "Username")
    password = forms.CharField(max_length=50, label = "Password", widget = forms.PasswordInput)
    confirm = forms.CharField(max_length = 50, label = "Confirm your password",widget = forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if User.objects.filter(username = username):
            raise forms.ValidationError("This username already taken !!!")
        if (confirm and password and (password != confirm)):
            raise forms.ValidationError("Passwords don't match")
        return {"username":username,"password":password}



    