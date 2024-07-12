from django.contrib.postgres.operations import UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):
    ...

    operations = [UnaccentExtension()]
    
    
    dependencies = [
        ('product', '0020_activate_unaccent_extention'),
    ]