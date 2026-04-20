from django.db import migrations
from django.utils.translation import gettext as _

from arches.app.models.models import Plugin


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("models", "11499_add_editlog_resourceinstance_idx"),
    ]

    def add_accessibility_plugin(apps, schema_editor):

        instance = Plugin(
            pluginid="289685d5-4d0a-4dbd-8107-78447cab67b9",
            name={"en": "Accessibility Plugin"},
            icon="fa fa-share-alt",
            component="views/components/plugins/accessibility",
            componentname="accessibility",
            config={
                "show": True,
                "description": {"en": None},
                "i18n_properties": ["description"],
            },
            slug="accessibility-plugin",
            sortorder=0,
        )

        instance.save()

    def remove_accessibility_plugin(apps, schema_editor):

        accessibility_plugin = Plugin.objects.get(
            pk="289685d5-4d0a-4dbd-8107-78447cab67b9"
        )

        accessibility_plugin.delete()

    operations = [
        migrations.RunPython(
            add_accessibility_plugin,
            remove_accessibility_plugin,
        ),
    ]
