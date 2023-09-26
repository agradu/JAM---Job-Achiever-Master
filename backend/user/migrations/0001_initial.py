# Generated by Django 4.2.5 on 2023-09-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
                ("name", models.CharField(max_length=50)),
                ("birthday", models.DateTimeField()),
                ("gender_id", models.CharField(max_length=50)),
                ("surname", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=100)),
                ("social_link", models.CharField(max_length=50)),
                ("portfolio_link", models.CharField(max_length=50)),
                ("api_key", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
