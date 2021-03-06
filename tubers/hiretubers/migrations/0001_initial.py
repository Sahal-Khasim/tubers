# Generated by Django 3.2.3 on 2021-06-02 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hiretuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('tuber_id', models.IntegerField(blank=True)),
                ('tuber_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=244)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(default='@gmail.com', max_length=254)),
                ('state', models.CharField(max_length=255)),
                ('message', models.TextField(blank=True)),
                ('user_id', models.IntegerField(blank=True)),
                ('created_date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
