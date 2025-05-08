import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"jersey_her"), "jersey_her.urls", name="jersey_her"),
)
