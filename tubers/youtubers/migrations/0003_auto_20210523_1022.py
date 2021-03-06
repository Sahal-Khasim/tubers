# Generated by Django 3.2.3 on 2021-05-23 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_remove_youtuber_is_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtubers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('photo', models.ImageField(upload_to='media/ytubers/Y%/m%/')),
                ('video_url', models.CharField(max_length=245)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('crew', models.CharField(max_length=244)),
                ('camera_type', models.CharField(max_length=255)),
                ('subs_count', models.CharField(max_length=244)),
                ('catagory', models.CharField(max_length=255)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Youtuber',
        ),
    ]
