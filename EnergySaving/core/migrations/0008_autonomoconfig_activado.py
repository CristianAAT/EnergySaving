# Generated by Django 2.2 on 2020-05-05 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_autonomoconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='autonomoconfig',
            name='activado',
            field=models.BooleanField(default=True, verbose_name='Activado'),
            preserve_default=False,
        ),
    ]
