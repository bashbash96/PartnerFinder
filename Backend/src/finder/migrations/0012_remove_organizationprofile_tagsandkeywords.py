# Generated by Django 2.2.7 on 2020-01-02 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0011_organizationprofile_tagsandkeywords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizationprofile',
            name='tagsAndKeywords',
        ),
    ]
