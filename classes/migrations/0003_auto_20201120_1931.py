# Generated by Django 2.2.14 on 2020-11-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20201120_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
