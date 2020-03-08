# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-03-08 09:13
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='avito_gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата создания')),
                ('npict', models.ImageField(upload_to='image/%Y/%m/%d/avito', verbose_name='Фото объекта')),
            ],
            options={
                'verbose_name': 'Выгрузки галерея (Avito)',
                'verbose_name_plural': 'Выгрузки галерея (Avito)',
            },
        ),
        migrations.CreateModel(
            name='avitoflats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateBegin', models.DateField(null=True, verbose_name='Дата начала размещения объявления:')),
                ('DateEnd', models.DateField(null=True, verbose_name='Дата окончания публикации объявления:')),
                ('Street', models.CharField(help_text='Например Гагарина', max_length=55, verbose_name='Улица:')),
                ('House_Numb', models.CharField(help_text='например 36', max_length=55, verbose_name='Номер дома:')),
                ('Description', models.TextField(verbose_name='Oписание объявления:')),
                ('Price', models.IntegerField(default=800000, validators=[django.core.validators.MinValueValidator(300000)], verbose_name='Цена в рублях:')),
                ('AdStatus', models.CharField(choices=[('Неопубликованно', 'Неопубликованно'), ('Обычное', 'Обычное'), ('Премиум-объявление', 'Премиум-объявление'), ('VIP-объявление', 'VIP-объявление'), ('Поднятие объявления в поиске', 'Поднятие объявления в поиске'), ('Выделение объявления', 'Выделение объявления'), ('Турбо-продажа', 'Турбо-продажа'), ('Быстрая продажа', 'Быстрая продажа')], max_length=55, verbose_name='Платная услуга:')),
                ('Rooms', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество комнат в квартире:')),
                ('Square', models.IntegerField(validators=[django.core.validators.MinValueValidator(10)], verbose_name='Общая площадь объекта:')),
                ('Floor', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Этаж:')),
                ('Floors', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Количество этажей в доме:')),
                ('HouseType', models.CharField(choices=[('Кирпичный', 'Кирпичный'), ('Панельный', 'Панельный'), ('Блочный', 'Блочный'), ('Монолитный', 'Монолитный'), ('Деревянный', 'Деревянный')], max_length=35, verbose_name='Тип дома:')),
                ('MarketType', models.CharField(choices=[('Вторичка', 'Вторичка'), ('Новостройка', 'Новостройка')], max_length=35, verbose_name='Принадлежность квартиры к рынку:')),
                ('auth', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Выгрузка на Авито',
                'verbose_name_plural': 'Выгрузка на Авито',
            },
        ),
        migrations.AddField(
            model_name='avito_gallery',
            name='id_gal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idd_gal', to='avito.avitoflats', verbose_name='Название'),
        ),
    ]
