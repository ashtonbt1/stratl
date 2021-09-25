from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Player, Hitter, Pitcher, Position, RollResult

# Register your models here.
@admin.register(Player)
class PlayerAdmin(ImportExportModelAdmin):
    pass

class PositionInline(admin.TabularInline):
    model = Position


class RollResultInline(admin.TabularInline):
    model = RollResult


@admin.register(Hitter)
class HitterAdmin(ImportExportModelAdmin):
    inlines = [
        PositionInline,
        RollResultInline,
    ]


@admin.register(Pitcher)
class PitcherAdmin(ImportExportModelAdmin):
    inlines = [
        RollResultInline,
    ]

@admin.register(Position)
class PositionAdmin(ImportExportModelAdmin):
    model = Position


@admin.register(RollResult)
class RollResultAdmin(ImportExportModelAdmin):
    model = RollResult