# Imports
from django.core.management.base import BaseCommand, CommandError
from arches.app.models.resource import Resource
from arches.app.models.tile import Tile
# Command class, inherit from arches BaseCommand
class Command(BaseCommand):

    # Self and optional variables required
    def handle (self, *args, **options):

#        res = Resource.objects.get(pk="a106c400-260c-11e7-a604-14109fd34195")
 #       res.load_tiles()
  #      for tile in res.tiles:
   #         for k,v in tile.data.items():
    #            if k == 'feb96005-fa14-11e6-aa8d-6c4008b05c4c':
     #               for each in v:
      #                  print(each)
       #                 each['url'] = each['url'].replace("/files/uploadedfiles/", "https://jerseyv6-arches-media.s3.eu-west-2.amazonaws.com/files/")
        #                print(each)
         #               res.save()


        tiles = Tile.objects.filter(nodegroup_id="feb95991-fa14-11e6-974f-6c4008b05c4c")
        for tile in tiles:
            for k,v in tile.data.items():
                if k == 'feb96005-fa14-11e6-aa8d-6c4008b05c4c':
                    for each in v:
                        print(each)
                        each['url'] = each['url'].replace("/files/uploadedfiles/", "https://jerseyv6-arches-media.s3.eu-west-2.amazonaws.com/files/")
                        print(each)
                        tile.save()
