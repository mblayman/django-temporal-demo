# Generated by Django 4.2.6 on 2023-11-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_polical_parties"),
    ]

    operations = [
        migrations.AddField(
            model_name="escrow",
            name="amount",
            field=models.IntegerField(default=0, help_text="Amount to store in cents"),
        ),
    ]
