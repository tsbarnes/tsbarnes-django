# Generated by Django 2.2.3 on 2019-08-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20190805_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinfo',
            name='avatar',
            field=models.ImageField(blank=True, default='no-img.gif', upload_to=''),
        ),
    ]