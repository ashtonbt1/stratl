from django.contrib import admin
from .models import Player, Hitter, Pitcher

# Register your models here.
admin.site.register([Player, Hitter, Pitcher])