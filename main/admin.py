from django.contrib import admin

from .models import DataModel


class DataModelAdmin(admin.ModelAdmin):
    exclude = ()
    readonly_fields = ('encrypted', )


admin.site.register(DataModel, DataModelAdmin)
