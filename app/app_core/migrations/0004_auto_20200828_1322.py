# Generated by Django 3.1 on 2020-08-28 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_core', '0003_ingredientmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IngredientModel',
            new_name='Ingredient',
        ),
    ]
