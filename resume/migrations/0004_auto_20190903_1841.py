# Generated by Django 2.2.3 on 2019-09-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20190825_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Company URL'),
        ),
    ]
