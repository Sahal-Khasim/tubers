# Generated by Django 3.2.3 on 2021-05-20 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0005_alter_team_youtube_channel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='insta_link',
            new_name='linkdin_link',
        ),
    ]
