# Generated by Django 2.2 on 2020-04-15 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200408_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrominuto',
            name='created',
            field=models.DateTimeField(verbose_name='Fecha de creación'),
        ),
    ]
