from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_password(self):
        return self.initial['password']


class SpecialUserForm(forms.Form):
    email = forms.EmailField(label="ایمیل", widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(label="نام", widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="نام خانوادگی", widget=forms.TextInput(attrs={"class": "form-control"}))
    company = forms.CharField(label="نام شرکت", widget=forms.TextInput(attrs={"class": "form-control"}))
    activity_field = forms.CharField(label="زمینه فعالیت", widget=forms.TextInput(attrs={"widget": "form-control"}))
    position = forms.CharField(label="سمت", widget=forms.TextInput(attrs={"class": "form-control"}))
    phone_number = forms.CharField(label="شماره تلفن", max_length=11,
                                   widget=forms.TextInput(attrs={"class": "form-control"}))
    pin = forms.CharField(label="PIN", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    description = forms.Textarea(label="توضیحات")


class LoginForm(forms.Form):
    email = forms.EmailField(label="ایمیل", widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.EmailField(label="رمز عبور", widget=forms.EmailInput(attrs={"class": "form-control"}))
