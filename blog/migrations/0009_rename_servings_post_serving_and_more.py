# Generated by Django 4.2.16 on 2024-12-09 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_category_post_servings_post_timings_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='servings',
            new_name='serving',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='timings',
            new_name='timing',
        ),
    ]