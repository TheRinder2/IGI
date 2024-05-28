from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from RealtorBack.models import Comment
from .models import User as MyUser


class UserRegisterForm(UserCreationForm):
    age = forms.IntegerField(min_value=18, max_value=99)
    fullName = forms.CharField()
    phone = forms.CharField()
    passport = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        if commit:
            user.save()
            MyUser.objects.create(
                user=user,
                age=self.cleaned_data['age'],
                fullName=self.cleaned_data['fullName'],
                phone=self.cleaned_data['phone'],
                passport=self.cleaned_data['passport'],
                isworker=False
            )
        return user

class UserEditForm(forms.Form):

    age = forms.IntegerField()
    fullName = forms.CharField()
    phone = forms.CharField()
    passport = forms.CharField()

    def save(self, user, commit=True):
        if commit:
            us = MyUser.objects.filter(user=user)[0]
            us.age = self.cleaned_data['age']
            us.fullName = self.cleaned_data['fullName']
            us.phone = self.cleaned_data['phone']
            us.passport = self.cleaned_data['passport']
            us.save()
        return user

