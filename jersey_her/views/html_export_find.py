from django.shortcuts import render
from arches.app.models.resource import Resource
from arches.app.utils.data_management.resources.exporter import ResourceExporter
from arches.app.utils import import_class_from_string
from arches.app.models.system_settings import settings
from arches.app.utils.data_management.resources.formats.htmlfile import HtmlWriter
from uuid import UUID


def html_export_find(request):

    html_writer = HtmlWriter()

    resource_instance_id = "ea45e9ee-50e0-418d-b13a-0c3909239287"
    # resource_instance_id = "2fabe289-16c0-484f-a9a1-1280a924f0c7"

    resource_list = html_writer.fetch_resource_objects_list(
        resourceinstanceids=[resource_instance_id],
        allowed_graph_ids=["3af584c3-fd4d-11e6-9e3e-026d961c88e6"],
    )

    resource = resource_list["3af584c3-fd4d-11e6-9e3e-026d961c88e6"][0]

    return render(
        request,
        "html_export/html_export_find.htm",
        {"resources": [resource]},
    )
