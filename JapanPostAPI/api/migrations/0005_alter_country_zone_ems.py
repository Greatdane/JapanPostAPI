# Generated by Django 3.2.2 on 2021-05-13 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_country_zone_ems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='zone_EMS',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
