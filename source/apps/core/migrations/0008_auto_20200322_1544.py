# Generated by Django 3.0.2 on 2020-03-22 15:44

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_reportcssegismodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reportcssegismodel',
            options={'verbose_name': 'CSSEGIS Report'},
        ),
        migrations.AlterField(
            model_name='reportcssegismodel',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(x=112.2707, y=30.9756), srid=4326),
        ),
    ]
