# Generated by Django 4.2.9 on 2024-05-27 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_alter_product_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]
