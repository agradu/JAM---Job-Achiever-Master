# Generated by Django 4.2.5 on 2023-09-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_rename_user_id_education_user_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birthday",
            field=models.DateField(),
        ),
    ]
