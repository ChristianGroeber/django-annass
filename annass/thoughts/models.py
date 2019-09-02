from django.db import models

# Create your models here.
from django.db.models import DateTimeField
from django.utils import timezone
from martor.models import MartorField


class Thought(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titel')
    content = MartorField(blank=True, verbose_name="Text")
    date_posted = DateTimeField(default=timezone.now, verbose_name='Datum geposted')

    def __str__(self):
        return self.title
