# Generated by Django 3.2.3 on 2021-06-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hiretuber',
            name='email',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hiretuber',
            name='state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hiretuber',
            name='tuber_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hiretuber',
            name='tuber_name',
            field=models.CharField(max_length=100),
        ),
    ]
