# Imports
from django.core.management.base import BaseCommand, CommandError
from arches.app.models.tile import Tile
from django.db.models import Q
import re


class Command(BaseCommand):
    """
    Excel removes 0's from the start of numbers because it's annoying.
    This script re-adds them.
    """

    def handle(self, *arg, **options):

        # function for checking len and performing changes
        def scan_and_add(value_to_change):
            if (
                len(value_to_change) != 7
            ):  # this will get in all < but also those with decimals and >

                if re.match(
                    "^[0-9\.]*$", value_to_change
                ):  # check HER number is actually a number and no letters in

                    if "." in value_to_change:
                        before_dot = value_to_change.split(".")
                        if len(before_dot[0]) != 7:
                            value_to_change = "0" + value_to_change
                            return value_to_change

                    else:
                        value_to_change = "0" + value_to_change
                        return value_to_change

        #     ngroup_dict = {'b9e90911-e741-11e6-84a6-026d961c88e6' : 'cc56798c-2e44-11ea-8326-0275d4869ef4', # Activity ngroup and node
        #                    'b712af77-fd4d-11e6-9e3e-026d961c88e6' : '45bfc38c-33d1-11ea-8701-0275d4869ef4', # Finds
        #                    '574b58a3-e747-11e6-84a6-026d961c88e6' : '818ec4ae-2e44-11ea-8326-0275d4869ef4', # Heritage Asset
        #                    'aa4096f1-e74a-11e6-84a6-026d961c88e6' : '03a2f1d6-2e45-11ea-8326-0275d4869ef4', # Info resource
        #                    }

        ngroup_dict = {
            "574b58a3-e747-11e6-84a6-026d961c88e6": "818ec4ae-2e44-11ea-8326-0275d4869ef4",  # Heritage Asset
            "b9e90911-e741-11e6-84a6-026d961c88e6": "cc56798c-2e44-11ea-8326-0275d4869ef4",  # Activity ngroup and node
            "b712af77-fd4d-11e6-9e3e-026d961c88e6": "45bfc38c-33d1-11ea-8701-0275d4869ef4",  # Finds
            "aa4096f1-e74a-11e6-84a6-026d961c88e6": "03a2f1d6-2e45-11ea-8326-0275d4869ef4",  # Info resource
        }

        for ngroups, node_keys in ngroup_dict.items():
            tiles = tiles = Tile.objects.filter(nodegroup_id=ngroups)

            for tile in tiles:
                if node_keys in tile.data:

                    new_v = scan_and_add(tile.data[node_keys])
                    if new_v != None:
                        tile.data[node_keys] = new_v

                    # print(tile.data[node_keys])

                    tile.save()
