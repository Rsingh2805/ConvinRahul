from django.contrib import admin

from .models import DataModel


class DataModelAdmin(admin.ModelAdmin):
    exclude = ()


admin.site.register(DataModel, DataModelAdmin)
