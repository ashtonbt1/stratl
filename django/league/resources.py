from import_export import resources
from .models import Player


class PlayerResource(resources.ModelResource):

    class Meta:
        model = Player
