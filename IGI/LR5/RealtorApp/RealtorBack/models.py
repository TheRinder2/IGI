from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Contact(models.Model):
    full_name = models.TextField('ФИО')
    phone = models.TextField('Номер телефона')
    description = models.TextField('Описание')
    img = models.ImageField(upload_to='article', null=True)

    def __str__(self):
        return self.full_name


class FAQ(models.Model):
    question = models.TextField('Вопрос')
    answer = models.TextField('Ответ')
    date = models.DateField('Дата добавления')


class New(models.Model):
    title = models.TextField('Заголовок')
    text = models.TextField('Текст')

    def __str__(self):
        return self.title


class Vacancion(models.Model):
    title = models.TextField('Заголовок')
    text = models.TextField('Текст')
    cost = models.IntegerField('Стоимость услуг', default=0)

    def __str__(self):
        return self.title


class Discount(models.Model):
    title = models.TextField('Заголовок')
    text = models.TextField('Текст')

    def __str__(self):
        return self.title


class Rent(models.Model):
    responsuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField('Услуга')
    cost = models.IntegerField('Цена')
    duration = models.DateTimeField('Длительность аренды')


class Immovables(models.Model):
    responsuser = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField('Описание')
    tp = models.TextField('')
    cost = models.IntegerField('Цена')

    def __str__(self):
        return self.text


class RequestRent(models.Model):
    rent = models.ForeignKey(Rent, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ready = models.BooleanField("Заказ выполнен", default=False)


class RequestImm(models.Model):
    imm = models.ForeignKey(Immovables, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ready = models.BooleanField("Заказ выполнен", default=False)


class Comment(models.Model):
    text = models.TextField('Текст комментария')
    data = models.DateTimeField('Время комментария', default=timezone.now)
    mark = models.IntegerField('Оценка')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.data.strftime('%S:%M:%H %d/%m/%Y')


class Time(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Report(models.Model):
    text = models.TextField('Отчёт')
    userId = models.IntegerField('Id работника')
