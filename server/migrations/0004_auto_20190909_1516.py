# Generated by Django 2.2.5 on 2019-09-09 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20190909_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='vehicle_ids',
            new_name='vehicle_id',
        ),
    ]
