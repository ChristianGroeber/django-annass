from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget

from .models import BlogEntry


# Register your models here.


def activate(modeladmin, request, queryset):
    queryset.update(active=True)


def deactivate(modeladmin, request, queryset):
    queryset.update(active=False)


activate.short_description = "Aktivieren"
deactivate.short_description = "Deaktivieren"


class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }
    exclude = ('date_posted', )
    list_display = ('title', 'date_posted', 'active')
    actions = [activate, deactivate]


admin.site.register(BlogEntry, YourModelAdmin)
