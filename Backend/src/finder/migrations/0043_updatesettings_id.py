# Generated by Django 2.2.10 on 2020-05-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0042_alertssettings_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='updatesettings',
            name='ID',
            field=models.IntegerField(default=1, unique=True),
        ),
    ]
