# Generated by Django 2.1.3 on 2018-11-19 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20181119_0626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moda',
            name='model',
        ),
        migrations.AlterField(
            model_name='cars',
            name='make',
            field=models.CharField(choices=[('bmw', 'BMW'), ('mercedes', 'MERCEDES BENZ'), ('toyota', 'TOYOTA'), ('honda', 'HONDA'), ('hyundai', 'HYUNDAI'), ('acura', 'ACURA'), ('nissan', 'NISSAN'), ('audi', 'AUDI'), ('mazda', 'MAZDA'), ('dodge', 'DODGE'), ('ford', 'FORD'), ('kia', 'KIA')], max_length=200),
        ),
        migrations.DeleteModel(
            name='Make',
        ),
        migrations.DeleteModel(
            name='Moda',
        ),
    ]
