# Imports
from django.core.management.base import BaseCommand, CommandError
from arches.app.models.tile import Tile

class Command(BaseCommand):

    '''
    Remove finders name from all Find resources
    '''

    def handle(self, *arg, **options):

        tiles = Tile.objects.filter(nodegroup_id = "26243e3f-fd58-11e6-9e3e-026d961c88e6")
        for tile in tiles:
            key = "26243e43-fd58-11e6-9e3e-026d961c88e6"
            if key in tile.data:
                val = tile.data[key]
                if val is not None:
                    tile.data[key] = None
                    print(tile.data[key])
                    tile.save()
