# Generated by Django 4.2.7 on 2023-11-15 00:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("runner", "0004_checkpoint_delete_checkpoints"),
    ]

    operations = [
        migrations.AlterField(
            model_name="checkpoint",
            name="time",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
