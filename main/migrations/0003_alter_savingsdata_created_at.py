# Generated by Django 5.1.2 on 2024-11-07 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_savingsdata_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="savingsdata",
            name="created_at",
            field=models.DateField(auto_now_add=True),
        ),
    ]
