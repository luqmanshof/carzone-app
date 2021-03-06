# Generated by Django 3.0.7 on 2020-09-19 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200916_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='linkedin_link',
            field=models.URLField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='google_plus_link',
            field=models.URLField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(default='', max_length=100),
        ),
    ]
