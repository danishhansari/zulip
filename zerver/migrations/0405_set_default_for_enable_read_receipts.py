# Generated by Django 4.0.6 on 2022-08-08 16:52

from django.db import migrations
from django.db.backends.postgresql.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps
from django.db.models import Q


def set_default_for_enable_read_receipts(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    Realm = apps.get_model("zerver", "Realm")
    # We enable read receipts by default in realms which require an invitation to
    # join or which allow only users having emails with specific domains to join.
    Realm.objects.filter(Q(invite_required=True) | Q(emails_restricted_to_domains=True)).update(
        enable_read_receipts=True
    )


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0404_realm_enable_read_receipts"),
    ]

    operations = [
        migrations.RunPython(set_default_for_enable_read_receipts, elidable=True),
    ]
