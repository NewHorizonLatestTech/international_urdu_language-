# Generated by Django 4.1.3 on 2022-11-24 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("urdu", "0005_alter_school_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="school",
            name="photo",
            field=models.ImageField(upload_to="myimage"),
        ),
    ]