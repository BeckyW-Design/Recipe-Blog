# Generated by Django 4.2.16 on 2024-12-11 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_upload', '0002_recipeupload_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeupload',
            name='status',
        ),
    ]
