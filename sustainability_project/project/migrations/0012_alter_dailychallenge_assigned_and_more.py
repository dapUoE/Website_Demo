# Generated by Django 5.0.1 on 2024-02-24 21:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_alter_dailychallenge_assigned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailychallenge',
            name='assigned',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 24, 21, 21, 14, 733979, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='userchallenges',
            name='submitted',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 24, 21, 21, 14, 734201, tzinfo=datetime.timezone.utc)),
        ),
    ]
