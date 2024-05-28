from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField('Возраст')
    fullName = models.TextField('ФИО')
    phone = models.TextField('Номер')
    passport = models.TextField('Паспорт')
    isworker = models.BooleanField('Работник', default=False)

    def __str__(self):
        return self.user.username
