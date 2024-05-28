import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from dateutil.relativedelta import relativedelta


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, validators=[
                                      MaxValueValidator(
                                          limit_value=datetime.date.today() - relativedelta(years=18),
                                          message="You must be 18 y.o or older!"),
                                      MinValueValidator(
                                          limit_value=datetime.date.today() - datetime.timedelta(days=120 * 365),
                                          message="You must enter your real age!")])
    fullName = models.TextField('ФИО')
    phone = models.TextField('Номер')
    passport = models.TextField('Паспорт')
    isworker = models.BooleanField('Работник', default=False)

    def __str__(self):
        return self.user.username
