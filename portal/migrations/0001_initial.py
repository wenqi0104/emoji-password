# Generated by Django 4.1.7 on 2023-03-01 17:40

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
                ("username", models.CharField(max_length=128, unique=True)),
                ("password", models.CharField(max_length=256)),
                ("createAt", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
