# Generated by Django 2.2.10 on 2020-05-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0041_auto_20200526_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertssettings',
            name='ID',
            field=models.IntegerField(default=1, unique=True),
        ),
    ]
