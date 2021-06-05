from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField



class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.IntegerField(blank=True)
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    created_date = models.DateField(blank=True, default=datetime.now)


    def __str__(self):
        return self.email


class Address(models.Model):
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    address = RichTextField(
    )

    def __str__(self):
        return self.email