from django.contrib import admin
from django.db import models
from django.forms import forms
from django.forms.widgets import Input, NumberInput

from .models import Person, Country, City
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = ('FirstName', 'FamilyName', 'Patronymic', 'Gender', 'Age', 'Job', 'Salary', 'PhoneNumber', 'PostCode', 'Countries', 'Cities')
    list_display = ('FirstName', 'FamilyName', 'Patronymic', 'Gender', 'Age', 'Job', 'Salary', 'PhoneNumber', 'PostCode', 'Countries', 'Cities')
    search_fields = ('FirstName', 'FamilyName', 'Patronymic', 'Gender', 'Age', 'Job', 'Salary', 'PhoneNumber', 'PostCode')

    formfield_overrides = {
        models.IntegerField: {
            'widget': NumberInput(attrs={'id': '2', 'class': 'width: 100px'})},
    }


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ('Name',)
    search_fields = ('Name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ('Name', 'Countries')
    search_fields = ('Name', 'Countries')