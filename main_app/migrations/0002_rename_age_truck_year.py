# Generated by Django 4.1.4 on 2022-12-21 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="truck",
            old_name="age",
            new_name="year",
        ),
    ]
