# Generated by Django 2.2.7 on 2020-01-06 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0025_auto_20200105_2123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='organization',
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
