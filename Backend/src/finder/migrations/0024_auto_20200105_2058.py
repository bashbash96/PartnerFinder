# Generated by Django 2.2.7 on 2020-01-05 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0023_auto_20200104_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizationprofile',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finder.Address'),
        ),
    ]