# Generated by Django 4.1.4 on 2022-12-22 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0007_truck_mods"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mod",
            old_name="age",
            new_name="skill",
        ),
    ]
