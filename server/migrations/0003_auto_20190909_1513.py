# Generated by Django 2.2.5 on 2019-09-09 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20190909_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='status',
            field=models.CharField(choices=[('disconnected', 'disconnected'), ('connected', 'connected')], max_length=20),
        ),
    ]
