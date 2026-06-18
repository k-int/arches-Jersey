# Imports
from django.core.management.base import BaseCommand, CommandError
from arches.app.models.resource import Resource
from arches.app.models.tile import Tile

from arches.app.models.models import Concept as modelConcept
from arches.app.models.concept import Concept
from arches.app.models.models import Value
from arches.app.utils.skos import SKOSWriter, SKOSReader


# Command class, inherit from arches BaseCommand
class Command(BaseCommand):

    # Self and optional variables required
    def handle(self, *args, **options):

        # conceptSchemes = modelConcept.objects.filter(nodetype='ConceptScheme').values_list('conceptid', flat=True)
        conceptids = [
            str(c.conceptid)
            for c in modelConcept.objects.filter(nodetype="ConceptScheme")
        ]

        concept_graphs = []

        for conceptid in conceptids:
            concept_graphs.append(
                Concept().get(
                    id=conceptid,
                    include_subconcepts=True,
                    include_parentconcepts=False,
                    include_relatedconcepts=True,
                    depth_limit=None,
                    up_depth_limit=None,
                )
            )

        for concept_graph in concept_graphs:
            prefLabel = Value.objects.get(
                concept_id=concept_graph.id, valuetype="prefLabel"
            ).value
            skos_xml = SKOSWriter().write(concept_graph, format="pretty-xml")
            with open(f"../thesauri/{prefLabel}.xml", "w", encoding="utf-8") as f:
                f.write(skos_xml.decode("utf-8"))
