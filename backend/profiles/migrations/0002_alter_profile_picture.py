# Generated by Django 4.2.5 on 2023-10-11 07:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="saved_files/profile_pictures/"
            ),
        ),
    ]
