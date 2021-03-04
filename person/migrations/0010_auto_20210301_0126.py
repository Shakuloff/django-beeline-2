# Generated by Django 3.1.7 on 2021-02-28 19:26

from django.db import migrations, models
import person.models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0009_person_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Age',
            field=models.IntegerField(default='63', verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Gender',
            field=models.CharField(choices=[('Женский', 'Женский'), ('Мужской', 'Мужской')], default='Мужской', max_length=10, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='person',
            name='Salary',
            field=models.IntegerField(default=person.models.random_salary, verbose_name='Зарплата'),
        ),
    ]
