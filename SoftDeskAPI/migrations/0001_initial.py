# Generated by Django 5.0 on 2023-12-15 10:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Comment",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("content", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Contributor",
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
            ],
        ),
        migrations.CreateModel(
            name="Issue",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("in_progress", "In Progress"),
                            ("resolved", "Resolved"),
                            ("cancelled", "Cancelled"),
                        ],
                        default="in_progress",
                        max_length=20,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("low", "Low"),
                            ("medium", "Medium"),
                            ("high", "High"),
                        ],
                        default="medium",
                        max_length=20,
                    ),
                ),
                (
                    "tag",
                    models.CharField(
                        choices=[
                            ("bug", "Bug"),
                            ("task", "Task"),
                            ("improvement", "Improvement"),
                        ],
                        default="bug",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
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
                ("name", models.CharField(max_length=255)),
                (
                    "project_type",
                    models.CharField(
                        choices=[
                            ("back-end", "Back-end"),
                            ("front-end", "Front-end"),
                            ("iOS", "iOS"),
                            ("Android", "Android"),
                        ],
                        max_length=20,
                    ),
                ),
                ("description", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
