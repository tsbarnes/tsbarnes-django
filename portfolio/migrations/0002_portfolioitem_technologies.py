# Generated by Django 2.2.3 on 2019-07-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioitem',
            name='technologies',
            field=models.TextField(blank=True),
        ),
    ]
