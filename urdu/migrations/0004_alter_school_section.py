# Generated by Django 4.1.3 on 2022-11-23 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("urdu", "0003_delete_testmodel_school_language_to_learn_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="school",
            name="section",
            field=models.CharField(default="", max_length=50),
        ),
    ]
