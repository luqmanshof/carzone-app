# Generated by Django 3.0.7 on 2020-09-27 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20200919_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
