# Generated by Django 3.1 on 2020-08-29 18:05

import app_core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0005_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=app_core.models.recipe_image_file_path),
        ),
    ]
