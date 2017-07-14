from __future__ import unicode_literals

from django.db import migrations

def load_zuora(apps, schema_editor):
    User = apps.get_model("webapp", "User")
    zuora = User(id=0, name = "Corporate", email = 'donations@zuora.com')
    zuora.save()

class Migration(migrations.Migration):

    dependencies = [
    ('webapp', '0001_initial'),]

    operations = [
        migrations.RunPython(load_zuora),
    ]

