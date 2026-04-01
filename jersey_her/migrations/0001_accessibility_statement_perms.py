from django.db import migrations
from django.utils.translation import gettext as _


class Migration(migrations.Migration):

    initial = True

    # dependencies = [("arches_her", "0001_initial")]

    add_accessibility_statement_perms = """
        insert into guardian_groupobjectpermission (
            object_pk,
            content_type_id,
            group_id,
            permission_id)
        values (
            '289685d5-4d0a-4dbd-8107-78447cab67b9',
            53,
            8,
            213); 
    """

    remove_accessibility_statement_perms = """
        delete from guardian_groupobjectpermission where 
        object_pk = '289685d5-4d0a-4dbd-8107-78447cab67b9' and
        content_type_id = 53 and
        group_id = 8 and
        permission_id = 213;
    """

    operations = [
        migrations.RunSQL(
            add_accessibility_statement_perms,
            remove_accessibility_statement_perms,
        ),
    ]
