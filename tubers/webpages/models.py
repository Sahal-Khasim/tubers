from django.db import models
from ckeditor.fields import RichTextField



class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    button_link = models.URLField(max_length = 200, default='link')
    photo = models.ImageField(upload_to='media/slider/%Y/')
    create_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.headline


class Team(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=25)
    role = models.CharField(max_length=255)
    fb_link = models.CharField(max_length=255)
    linkdin_link = models.CharField(max_length=255)
    youtube_channel = models.CharField(max_length=250, default='My Channel')
    youtube_link = models.CharField(max_length=300, default='link')
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.first_name


class Aboutus(models.Model):
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    description = RichTextField()



class Service(models.Model):
    description = RichTextField()
    photo = models.ImageField(upload_to='media/service/%Y/%m/')
    


class ServiceCard(models.Model):
    card_title = models.CharField(max_length=30)
    card_description = RichTextField()



