import martor
from django.db import models

# Create your models here.
from django.db.models import CharField, DateTimeField, ImageField
from django.utils import timezone
from martor.models import MartorField


class BlogEntry(models.Model):
    title = CharField(max_length=100, verbose_name='Titel')
    description = CharField(max_length=500, verbose_name="Einleitungstext", blank=True)
    main_image = ImageField(upload_to="main-images", null=True, blank=True, verbose_name='Hauptbild')
    content = MartorField(verbose_name='Text')
    date_posted = DateTimeField(default=timezone.now, verbose_name='Datum geposted')
    active = models.BooleanField(default=False, verbose_name='Aktiv?')
    on_home = models.BooleanField(default=False, verbose_name='Auf der Home Seite anzeigen?')

    def __str__(self):
        return self.title
