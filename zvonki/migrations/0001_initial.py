# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-03-08 09:14
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='zvonok',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_sozd', models.DateTimeField(verbose_name='Дата создания:')),
                ('tel', models.IntegerField(help_text='9881112233', verbose_name='Телефон')),
                ('raion', multiselectfield.db.fields.MultiSelectField(choices=[('Выбор района', 'Выбор района'), ('Ахун', 'Ахун'), ('Бытха', 'Бытха'), ('Виноградная', 'Виноградная'), ('Дагомыс', 'Дагомыс'), ('Донская', 'Донская'), ('Донская(Пасечная)', 'Донская(Пасечная)'), ('Донская(Тимерязева)', 'Донская(Тимерязева)'), ('Завокзальный', 'Завокзальный'), ('Заречный', 'Заречный'), ('Клубничная', 'Клубничная'), ('КСМ', 'КСМ'), ('Красная поляна', 'Красная поляна'), ('Кудепста', 'Кудепста'), ('Макаренко', 'Макаренко'), ('Мамайка', 'Мамайка'), ('Мамайский перевал', 'Мамайский перевал'), ('Мацеста', 'Мацеста'), ('Н.Сочи', 'Н.Сочи'), ('Объезная', 'Объезная'), ('Пластунская', 'Пластунская'), ('Приморье', 'Приморье'), ('Раздольное', 'Раздольное'), ('Светлана', 'Светлана'), ('Соболевка', 'Соболевка'), ('Транспортная', 'Транспортная'), ('Фабрициуса', 'Фабрициуса'), ('Хоста', 'Хоста'), ('Центр', 'Центр'), ('(А) Блиново(+Вес)', '(А) Блиново(+Вес)'), ('(А) Гол. дали', '(А) Гол. дали'), ('(А) Кур.гор(+Чкал)', '(А) Кур.гор(+Чкал)'), ('(А) Мирный', '(А) Мирный'), ('(А) Молдовка', '(А) Молдовка'), ('(А) Центр', '(А) Центр'), ('(А) Чай совхоз', '(А) Чай совхоз')], default='Неважно', max_length=20, verbose_name='Район')),
                ('subj', models.CharField(choices=[('Неважно', 'Неважно'), ('Студия', 'Студия'), ('Однокомнатная', 'Однокомнатная'), ('Двухкомнатная', 'Двухкомнатная'), ('Многокомнатная', 'Многокомнатная'), ('Дом', 'Дом'), ('Участок', 'Участок'), ('Коммерция', 'Коммерция')], default='Неважно', max_length=50, verbose_name='Что ищет:')),
                ('cena', models.IntegerField(default=800000, validators=[django.core.validators.MinValueValidator(300000)], verbose_name='Бюджет до:')),
                ('client_name', models.CharField(max_length=45, verbose_name='Имя клиента:')),
                ('prim', models.TextField(verbose_name='Первичная информация:')),
                ('coment', models.TextField(verbose_name='Коментарий по проделанной работе')),
                ('status_zvonka', models.CharField(choices=[('Новый', 'Новый'), ('Перезвонить', 'Перезвонить'), ('Недозвонился', 'Недозвонился'), ('В работе', 'В работе'), ('Архив', 'Архив'), ('В общем доступе', 'В общем доступе')], default='Новый', max_length=55, verbose_name='Статус звонка')),
                ('prezvonit', models.DateTimeField(verbose_name='Перезвонить: ')),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Риелтор:')),
            ],
            options={
                'verbose_name': 'Звонки риелторам',
                'verbose_name_plural': 'Звонки риелторам',
            },
        ),
    ]
