# Imports
from django.core.management.base import BaseCommand, CommandError
from arches.app.models.tile import Tile

class Command(BaseCommand):

    '''
    Some zeros are missing from the front of HER numbers
    '''

    def handle(self, *arg, **options):
        
        # Activity Model
        a_wrong = []
        a_correct = []
        tiles = Tile.objects.filter(nodegroup_id = "b9e90911-e741-11e6-84a6-026d961c88e6")
        for tile in tiles:
            key = "cc56798c-2e44-11ea-8326-0275d4869ef4"
            if key in tile.data:
                
                val = tile.data[key]
                
                if val is not None:
                    if len(val) != 7:
                        a_wrong.append(val)
                    else:
                        a_correct.append(val)
        print(len(a_wrong))
        print(len(a_correct))

        # Finds
        a_wrong = []
        a_correct = []
        tiles = Tile.objects.filter(nodegroup_id = "b712af77-fd4d-11e6-9e3e-026d961c88e6")
        for tile in tiles:
            key = "45bfc38c-33d1-11ea-8701-0275d4869ef4"        
            if key in tile.data:
                val = tile.data[key]
                if val is not None:
                    if len(val) != 7:
                        a_wrong.append(val)
                    else:
                        a_correct.append(val)
        print(len(a_wrong))
        print(len(a_correct))

        # Heritage Asset
        a_wrong = []
        a_correct = []
        tiles = Tile.objects.filter(nodegroup_id = "574b58a3-e747-11e6-84a6-026d961c88e6")
        for tile in tiles:
            key = "818ec4ae-2e44-11ea-8326-0275d4869ef4"
            if key in tile.data:
                val = tile.data[key]
                if val is not None:
                    if len(val) != 7:
                        a_wrong.append(val)
                    else:
                        a_correct.append(val)
        print(len(a_wrong))
        print(len(a_correct))

        # Information Resource
        a_wrong = []
        a_correct = []
        tiles = Tile.objects.filter(nodegroup_id = "aa4096f1-e74a-11e6-84a6-026d961c88e6")
        for tile in tiles:
            key = "03a2f1d6-2e45-11ea-8326-0275d4869ef4"
            if key in tile.data:
                val = tile.data[key]
                if val is not None:
                    if len(val) != 7:
                        a_wrong.append(val)
                    else:
                        a_correct.append(val)
        print(len(a_wrong))
        print(len(a_correct))
