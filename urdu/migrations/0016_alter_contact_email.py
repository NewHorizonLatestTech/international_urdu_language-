# Generated by Django 4.1.3 on 2022-11-29 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("urdu", "0015_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact", name="email", field=models.CharField(max_length=50),
        ),
    ]
