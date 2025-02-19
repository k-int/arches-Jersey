from importlib import resources
from arches.app.models.models import ResourceInstance
from arches.app.models.resource import Resource
from django.core.management.base import BaseCommand, CommandError
from arches.app.models.tile import Tile

class Command(BaseCommand):
    """
    Command for removing trailing zeros from HER Reference 
    """
    
    def handle(self, *args, **options):

        
                #get all resource's 
        resources = Resource.objects.filter(graph_id = '99417385-b8fa-11e6-84a5-026d961c88e6') #UUID For heritage Asset Graph
        
        #Grab tiles for each resource
        for res in resources:
            tiles = Tile.objects.filter(resourceinstance_id = res.resourceinstanceid)
            her_node_id = "818ec4ae-2e44-11ea-8326-0275d4869ef4"
            for tile in tiles:
                if her_node_id in tile.data.keys():
                    if '.' in tile.data[her_node_id]:
                        print(res.resourceinstanceid)
                        tile.data[her_node_id] = tile.data[her_node_id].split('.')[0]
                        print(tile.data[her_node_id])
                        tile.save()
                
            
                 #if tile.resourceinstance_id == "040e5ac0-149c-0138-c572-740f24312a1c":
                     #print("!")
                #if her_node_id in tile.data.keys():
                   # if '.' in tile.data[her_node_id]:
                      #  her_id = tile.data[her_node_id].split('.')[0]
                       # tile.data[
        
        #get all resrouce's
        
#        tiles = Tile.objects.all()
 #       for tile in tiles:
  #          print(vars(tile))
   #         break
       # res = Resource.objects.get(pk = '')
        #for r in res:
       # tile = Tile.objects.filter(resourceinstance_id = res.resourceinstanceid)
       # for t in tile:
           # if "818ec4ae-2e44-11ea-8326-0275d4869ef4" in t.data.keys():
               # print(vars(t))
        #resources.load_tiles()
       # print(vars(resources))
       # for t in resources.tiles:
       #     if '818ec4ae-2e44-11ea-8326-0275d4869ef4' in t.data.keys():
       #         print(vars(t))
       #         print(t.data['818ec4ae-2e44-11ea-8326-0275d4869ef4'])
