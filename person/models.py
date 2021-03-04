from random import random, randrange, randint
import secrets

from django.db import models
# from django.db.models.signals import post_save, post_delete
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


def random_age():
    return str(randint(12, 120))


def random_number():
    r = randint(1, 2)
    n200 = [220, 221, 222, 223, 225, 227]
    if r == 1:
        return str(996) + str(randint(770, 779)) + str(randint(0000000, 999999))
    else:
        return str(996) + str(secrets.choice(n200)) + str(randint(0000000, 999999))


def random_salary():
    return str(randint(40000, 150000))


def random_postcode():
    return str(randint(720000, 724205))


class Country(models.Model):
    Name = models.CharField(max_length=150, verbose_name='Название страны')

    def __str__(self):
        return str(self.Name)

    def get_cities(self):
        return self.city_set

    class Meta:
        verbose_name_plural = "Страны"
        verbose_name = "Страна"


class City(models.Model):
    Name = models.CharField(max_length=150, verbose_name='Название города')
    Countries = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name_plural = "Города"
        verbose_name = "Город"


class Person(models.Model):
    CHOICES = (
        ('Женский', 'Женский'),
        ('Мужской', 'Мужской'),
    )
    FirstName = models.CharField(max_length=150, verbose_name='Имя')
    FamilyName = models.CharField(max_length=150, verbose_name='Фамилия')
    Patronymic = models.CharField(max_length=150, verbose_name='Отчество', default="Не указано")
    Gender = models.CharField(max_length=10, verbose_name='Пол', default="Мужской", choices=CHOICES)
    Age = models.IntegerField(verbose_name='Возраст', default=random_age())
    Job = models.CharField(max_length=150, verbose_name='Работа', default='Неизвестно')
    Salary = models.IntegerField(verbose_name='Зарплата', default=random_salary)
    PhoneNumber = models.IntegerField(verbose_name='Номер телефона', default=random_number)
    Countries = models.ForeignKey(Country, verbose_name="Страна", on_delete=models.SET_NULL, null=True)
    Cities = models.ForeignKey(City, verbose_name="Город", on_delete=models.SET_NULL, null=True)
    PostCode = models.IntegerField(verbose_name='Индекс почты', default=random_postcode)

    def __str__(self):
        return str(self.FirstName)

    class Meta:
        verbose_name_plural = "Люди"
        verbose_name = "Человек"


# class Job(models.Model):
#     Name = models.CharField(max_length=150, verbose_name='Должность')
#
#     def __str__(self):
#         return str(self.Name)
#
#     class Meta:
#         verbose_name_plural = "Должности"
#         verbose_name = "Должность"