# Generated by Django 2.2.7 on 2020-01-02 19:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0004_auto_20200102_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationprofile',
            name='tagsAndKeywords',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None),
        ),
    ]
