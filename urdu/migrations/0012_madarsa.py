# Generated by Django 4.1.3 on 2022-11-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("urdu", "0011_alter_school_roll_no"),
    ]

    operations = [
        migrations.CreateModel(
            name="madarsa",
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
                ("name", models.CharField(default="", max_length=50)),
                ("father_name", models.CharField(default="", max_length=50)),
                ("gender", models.CharField(default="", max_length=50)),
                ("Class", models.CharField(default="", max_length=50)),
                ("section", models.CharField(default="", max_length=50)),
                ("roll_no", models.CharField(default="", max_length=50)),
                ("native_country", models.CharField(default="", max_length=50)),
                ("native_language", models.CharField(default="", max_length=50)),
                ("language_to_learn", models.CharField(default="", max_length=50)),
                ("photo", models.FileField(default="", upload_to="myimage")),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
