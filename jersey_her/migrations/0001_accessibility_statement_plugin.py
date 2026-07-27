from django.db import migrations
from django.utils.translation import gettext as _
from arches.app.utils.permission_backend import assign_perm, remove_perm
from django.contrib.auth.models import Group
from django.core.cache import caches


def add_accessibility_plugin(apps, schema_editor):

    Plugin = apps.get_model("models", "Plugin")

    if not Plugin.objects.filter(pk="289685d5-4d0a-4dbd-8107-78447cab67b9").exists():
        Plugin.objects.update_or_create(
            pluginid="289685d5-4d0a-4dbd-8107-78447cab67b9",
            name={"en": "Accessibility Plugin"},
            icon="fa fa-universal-access",
            component="views/components/plugins/accessibility",
            componentname="accessibility",
            config={
                "show": True,
                "description": {"en": None},
                "i18n_properties": ["description"],
            },
            slug="accessibility",
            sortorder=0,
        )

    guest_group = Group.objects.get(name="Guest")

    accessibility_plugin = Plugin.objects.get(pk="289685d5-4d0a-4dbd-8107-78447cab67b9")

    assign_perm("view_plugin", guest_group, accessibility_plugin)


def remove_accessibility_plugin(apps, schema_editor):

    Plugin = apps.get_model("models", "Plugin")
    guest_group = Group.objects.get(name="Guest")

    accessibility_plugin = Plugin.objects.get(pk="289685d5-4d0a-4dbd-8107-78447cab67b9")

    remove_perm("view_plugin", guest_group, accessibility_plugin)

    user_permission_cache = caches["user_permission"]
    if user_permission_cache:
        user_permission_cache.clear()

    accessibility_plugin.delete()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("models", "11499_add_editlog_resourceinstance_idx"),
    ]

    operations = [
        migrations.RunPython(
            add_accessibility_plugin,
            remove_accessibility_plugin,
        ),
    ]
