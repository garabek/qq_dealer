# Generated by Django 2.1.3 on 2018-11-18 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_cars_transmition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cars',
            old_name='transmition',
            new_name='transmission',
        ),
    ]
