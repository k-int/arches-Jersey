from django.db import migrations
from django.utils.translation import gettext as _
from arches.app.utils.permission_backend import assign_perm, remove_perm
from django.contrib.auth.models import Group
from arches.app.models.models import Plugin


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("jersey_her", "0001_accessibility_statement_plugin"),
    ]

    def add_accessibility_perms(apps, schema_editor):

        guest_group = Group.objects.get(name="Guest")

        accessibility_plugin = Plugin.objects.get(
            pk="289685d5-4d0a-4dbd-8107-78447cab67b9"
        )

        assign_perm("view_plugin", guest_group, accessibility_plugin)

    def remove_accessibility_perms(apps, schema_editor):

        guest_group = Group.objects.get(name="Guest")
        accessibility_plugin = Plugin.objects.get(
            pk="289685d5-4d0a-4dbd-8107-78447cab67b9"
        )

        remove_perm("view_plugin", guest_group, accessibility_plugin)

    operations = [
        migrations.RunPython(
            add_accessibility_perms,
            remove_accessibility_perms,
        ),
    ]
