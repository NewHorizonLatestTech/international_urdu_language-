# Generated by Django 4.1.3 on 2022-11-24 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("urdu", "0014_alter_madarsa_photo"),
    ]

    operations = [
        migrations.CreateModel(
            name="contact",
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
                ("email", models.CharField(default="", max_length=50)),
                ("name", models.CharField(default="", max_length=50)),
            ],
        ),
    ]