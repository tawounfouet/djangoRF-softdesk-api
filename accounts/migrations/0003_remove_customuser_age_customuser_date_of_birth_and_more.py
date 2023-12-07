# Generated by Django 5.0 on 2023-12-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_alter_customuser_age"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="age",
        ),
        migrations.AddField(
            model_name="customuser",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="consent_choice",
            field=models.BooleanField(default=False),
        ),
    ]