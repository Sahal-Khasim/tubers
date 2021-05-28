from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

class Youtubers(models.Model):

    crew_choices = (
        ('solo','solo'),
        ('small','small'),
        ('large','large'),
    )

    camera_choices = (
        ('sony','sony'),
        ('canon','canon'),
        ('nikon','nikon'),
        ('red','red'),
        ('fuji','fuji'),
        ('panasonic','panasonic'),
        ('other','other'),
    )

    catogory_choices = (
        ('coding','coding'),
        ('mobile','mobile'),
        ('vlog','vlog'),
        ('gaming','gaming'),
        ('fuji','fuji'),
        ('comedy','comedy'),
        ('cooking','cooking'),
        ('sports','sports'),
        ('fashion','fashion'),
        ('motovlog','motovlog'),
        ('film_makers','film_making'),
    )


    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='media/ytubers/Y%/m%/')
    video_url = models.CharField(max_length=245)
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.IntegerField()
    crew = models.CharField( choices=crew_choices, max_length=244)
    camera_type = models.CharField( choices=camera_choices, max_length=255)
    subs_count = models.CharField(max_length=244)
    catagory = models.CharField( choices=catogory_choices, max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)