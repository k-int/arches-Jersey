from django.core.management.base import BaseCommand, CommandError
from arches.app.models.resource import Resource
import json

"""
Removed the alternative names node from the place nodegroup in Finds, after moving alternative names on its own card
"""


class Command(BaseCommand):

    def handle(self, *arg, **options):

        find_resources = Resource.objects.filter(
            graph_id="3af584c3-fd4d-11e6-9e3e-026d961c88e6"
        )

        print(len(find_resources))

        for resource in find_resources:
            resource.load_tiles()
            for tile in resource.tiles:
                if str(tile.nodegroup_id) == "6b5d6a33-fd4d-11e6-9e3e-026d961c88e6":
                    tile.data = {}
                    tile.save()
                    # print(tile.data)
