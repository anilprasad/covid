# Generated by Django 3.0.2 on 2020-03-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200322_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcssegismodel',
            name='country',
            field=models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='Country/Region'),
        ),
    ]
