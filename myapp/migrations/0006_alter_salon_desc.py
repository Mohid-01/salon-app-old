# Generated by Django 5.1 on 2024-09-08 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_salon_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salon',
            name='desc',
            field=models.CharField(max_length=300),
        ),
    ]
