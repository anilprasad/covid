# Generated by Django 3.0.2 on 2020-03-24 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20200324_0919'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reportcssegismodel',
            unique_together={('country', 'location', 'state', 'city')},
        ),
    ]
