# Generated by Django 3.0.2 on 2020-03-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200322_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcssegismodel',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Last Update'),
        ),
    ]