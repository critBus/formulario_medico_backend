# Generated by Django 4.2.7 on 2024-06-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_blacklistedtokenaccess"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(default=True),
        ),
    ]
