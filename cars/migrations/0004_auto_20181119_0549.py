# Generated by Django 2.1.3 on 2018-11-19 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20181118_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='make',
            field=models.CharField(choices=[('bmw', 'BMW'), ('mercedes', 'Mercedes Benz'), ('toyota', 'TOYOTA'), ('honda', 'HONDA'), ('hyundai', 'HYUNDAI'), ('acura', 'ACURA'), ('nissan', 'NISSAN'), ('audi', 'AUDI'), ('mazda', 'MAZDA'), ('dodge', 'DODGE'), ('ford', 'FORD'), ('kia', 'KIA')], max_length=200),
        ),
    ]
