# Generated by Django 3.1 on 2020-09-22 22:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='наименование типа продукта')),
            ],
            options={
                'verbose_name': 'тип продуктов',
                'verbose_name_plural': 'типы продуктов',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='производитель')),
                ('product_types', models.ManyToManyField(to='producer.ProductType', verbose_name='типы продуктов')),
            ],
            options={
                'verbose_name': 'производитель',
                'verbose_name_plural': 'производители',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Номер телефона должен быть в формате: '+999999999'. доступно до 15 знаков.", regex='^\\+?1?\\d{9,15}$')], verbose_name='номер телефона')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producer.producer', verbose_name='производитель')),
            ],
            options={
                'verbose_name': 'номер телефона',
                'verbose_name_plural': 'номера телефонов',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, verbose_name='номер электронной почты')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producer.producer', verbose_name='производитель')),
            ],
            options={
                'verbose_name': 'номер электронной почты',
                'verbose_name_plural': 'номера электронной почты',
            },
        ),
    ]
