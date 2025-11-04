from arches.app.search.components.base import BaseSearchFilter
from django.utils.translation import get_language
from arches.app.models.models import SearchComponent

details = {
    "searchcomponentid": "6a2fe122-de54-4e44-8e93-b6a0cda7955c",
    "name": "Sort",
    "icon": "",
    "modulename": "sort_results.py",
    "classname": "SortResults",
    "type": "sort-results-type",
    "componentpath": "views/components/search/sort-results",
    "componentname": "sort-results",
    "config": {},
}


class SortResults(BaseSearchFilter):
    def append_dsl(self, search_query_object, **kwargs):
        if self.request.GET.get(self.componentname, None):
            sort_param = self.request.GET.get(self.componentname, None)
        else:
            sort_param = "asc"

        sort_field = "_script"
        sort_dsl = {
            "type": "number",
            "script": {
                "lang": "painless",
                "params": {
                    "order": [
                        "99417385-b8fa-11e6-84a5-026d961c88e6",
                        "243f8689-b8f6-11e6-84a5-026d961c88e6",
                        "24d7b54f-5464-11e9-a86b-000d3ab1e588",
                        "3af584c3-fd4d-11e6-9e3e-026d961c88e6",
                    ]
                },
                "source": "List order = params.order; int index = order.indexOf(doc['graph_id'].value); return index != -1 ? index : order.size();",
            },
        }

        sort_dsl["order"] = sort_param

        search_query_object["query"].sort(
            field=sort_field,
            dsl=sort_dsl,
        )
