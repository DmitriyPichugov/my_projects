from django.db import migrations
from django.db import models
import re

def convert_price_to_float(apps, schema_editor):
    Apartment = apps.get_model('main', 'Apartment')
    for apartment in Apartment.objects.all():
        price_str = apartment.price
        price_num = float(re.sub(r'[^0-9.]', '', price_str))
        apartment.price = price_num
        apartment.save()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='price',
            field=models.FloatField(),
        ),
        migrations.RunPython(convert_price_to_float),
    ]
