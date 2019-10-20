from django.contrib import admin
from martor.widgets import AdminMartorWidget
from django.db import models

from .models import Thought


# Register your models here.


class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    exclude = ('date_posted', )
    list_display = ('title', 'date_posted')


admin.site.register(Thought, YourModelAdmin)
