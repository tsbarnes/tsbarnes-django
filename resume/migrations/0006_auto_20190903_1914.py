# Generated by Django 2.2.3 on 2019-09-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20190903_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='school_url',
            field=models.URLField(blank=True, null=True, verbose_name='School URL'),
        ),
    ]
