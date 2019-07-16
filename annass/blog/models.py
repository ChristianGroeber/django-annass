import martor
from django.db import models

# Create your models here.
from django.db.models import CharField, DateTimeField
from django.utils import timezone
from martor.models import MartorField


class BlogEntry(models.Model):
    title = CharField(max_length=100)
    content = MartorField()
    date_posted = DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
