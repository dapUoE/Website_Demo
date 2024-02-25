# Generated by Django 5.0.1 on 2024-02-24 21:20

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_userchallenges_daily_challenge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailychallenge',
            name='assigned',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 24, 21, 20, 34, 836890, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='userchallenges',
            name='daily_challenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.dailychallenge'),
        ),
    ]
