# Generated by Django 4.2.6 on 2023-11-13 15:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
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
                ("name", models.TextField()),
                ("age", models.PositiveIntegerField()),
                ("fav_color", models.TextField()),
                ("is_friend", models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name="Contact",
        ),
    ]
