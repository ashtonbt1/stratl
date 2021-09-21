from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Player, Hitter, Pitcher

# Register your models here.
admin.site.register([Hitter, Pitcher])

@admin.register(Player)
class PlayerAdmin(ImportExportModelAdmin):
    pass