# Generated by Django 5.0.1 on 2024-03-19 22:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("project", "0007_rename_item_number_village_position_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_gamekeeper",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customuser",
            name="profile_picture",
            field=models.CharField(default="blank.jpeg", max_length=25),
        ),
        migrations.AlterField(
            model_name="dailychallenge",
            name="assigned",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 19, 22, 56, 2, 477842, tzinfo=datetime.timezone.utc
                ),
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="userchallenges",
            name="submitted",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 19, 22, 56, 2, 478038, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="village",
            name="purchased",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 3, 19, 22, 56, 2, 477397, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]