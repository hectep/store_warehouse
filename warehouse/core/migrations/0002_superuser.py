from django.db import migrations
from django.contrib.auth.models import User


def forwards_func(apps, schema_editor):
    User.objects.create_superuser(
        username='warehouse_admin',
        password='warehouse_admin',
        email='fake@email.com'
    )


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial')
    ]
    operations = [
        migrations.RunPython(forwards_func, ),
    ]
