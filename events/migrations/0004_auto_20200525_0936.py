# Generated by Django 3.0.6 on 2020-05-25 09:36

# Django
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20200525_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
