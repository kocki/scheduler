# Generated by Django 3.0.6 on 2020-05-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]