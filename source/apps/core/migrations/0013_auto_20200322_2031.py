# Generated by Django 3.0.2 on 2020-03-22 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20200322_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcssegismodel',
            name='confirmed',
            field=models.PositiveIntegerField(default=0, verbose_name='Confirmed'),
        ),
        migrations.AlterField(
            model_name='reportcssegismodel',
            name='deaths',
            field=models.PositiveIntegerField(default=0, verbose_name='Deaths'),
        ),
        migrations.AlterField(
            model_name='reportcssegismodel',
            name='recovered',
            field=models.PositiveIntegerField(default=0, verbose_name='Recovered'),
        ),
    ]
