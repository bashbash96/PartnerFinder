# Generated by Django 2.2.10 on 2020-06-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0050_auto_20200602_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapids',
            name='indexID',
            field=models.IntegerField(),
        ),
    ]
