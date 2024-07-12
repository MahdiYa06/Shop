from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations


class Migration(migrations.Migration):
    ...

    operations = [TrigramExtension()]
    
    
    dependencies = [
        ('product', '0019_tags_product_tags'),
    ]