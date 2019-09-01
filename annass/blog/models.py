import martor
from django.db import models

# Create your models here.
from django.db.models import CharField, DateTimeField, ImageField
from django.utils import timezone
from martor.models import MartorField


class BlogEntry(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=500, verbose_name="Einleitungstext", blank=True)
    # main_image = ImageField(upload_to="main-images")
    content = MartorField()
    date_posted = DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
