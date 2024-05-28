import datetime

from dateutil.relativedelta import relativedelta
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

from RealtorBack.models import Comment
from .models import User as MyUser


class UserRegisterForm(UserCreationForm):
    birth_date = forms.DateField(validators=[
                                      MaxValueValidator(
                                          limit_value=datetime.date.today() - relativedelta(years=18),
                                          message="You must be 18 y.o or older!"),
                                      MinValueValidator(
                                          limit_value=datetime.date.today() - datetime.timedelta(days=120 * 365),
                                          message="You must enter your real age!")])
    fullName = forms.CharField()
    phone_number_regex = RegexValidator(
        regex=r'^(?:\+375)?\((?:29|33|25|44)\)\d{7}$',
        message="Invalid phone number, format: +375(29)XXXXXXX")
    phone = forms.CharField(validators=[phone_number_regex], max_length=20)
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
                birth_date=self.cleaned_data['birth_date'],
                fullName=self.cleaned_data['fullName'],
                phone=self.cleaned_data['phone'],
                passport=self.cleaned_data['passport'],
                isworker=False
            )
        return user

class UserEditForm(forms.Form):

    birth_date = forms.DateField(validators=[
                                      MaxValueValidator(
                                          limit_value=datetime.date.today() - relativedelta(years=18),
                                          message="You must be 18 y.o or older!"),
                                      MinValueValidator(
                                          limit_value=datetime.date.today() - datetime.timedelta(days=120 * 365),
                                          message="You must enter your real age!")])
    fullName = forms.CharField()
    phone_number_regex = RegexValidator(
        regex=r'^(?:\+375)?\((?:29|33|25|44)\)\d{7}$',
        message="Invalid phone number, format: +375(29)XXXXXXX")
    phone = forms.CharField(validators=[phone_number_regex], max_length=20)
    passport = forms.CharField()

    def save(self, user, commit=True):
        if commit:
            us = MyUser.objects.filter(user=user)[0]
            us.birth_date = self.cleaned_data['birth_date']
            us.fullName = self.cleaned_data['fullName']
            us.phone = self.cleaned_data['phone']
            us.passport = self.cleaned_data['passport']
            us.save()
        return user

