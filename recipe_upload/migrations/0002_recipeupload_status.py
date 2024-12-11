# Generated by Django 4.2.16 on 2024-12-11 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeupload',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending Review'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10),
        ),
    ]
