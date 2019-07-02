from django.db import models

# Create your models here.
from martor.models import MartorField


class UeberMich(models.Model):
    text = MartorField()

    def __str__(self):
        return 'Über mich'
