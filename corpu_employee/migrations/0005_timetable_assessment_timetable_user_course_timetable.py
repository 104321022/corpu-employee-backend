# Generated by Django 4.2 on 2023-05-10 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("corpu_employee", "0004_alter_user_user_id_department"),
    ]

    operations = [
        migrations.CreateModel(
            name="Timetable",
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
                ("monday_time", models.JSONField()),
                ("tuesday_time", models.JSONField()),
                ("wednesday_time", models.JSONField()),
                ("thursday_time", models.JSONField()),
                ("friday_time", models.JSONField()),
                (
                    "course_code",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corpu_employee.course",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        blank=True,
                        default="",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corpu_employee.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Assessment",
            fields=[
                (
                    "assessment_id",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                (
                    "course_code",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="corpu_employee.course",
                    ),
                ),
                (
                    "employee_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="applicant",
                        to="corpu_employee.user",
                    ),
                ),
                (
                    "staff_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="creator",
                        to="corpu_employee.user",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="timetable",
            constraint=models.UniqueConstraint(
                fields=("user_id", "course_code"), name="user_course_timetable"
            ),
        ),
    ]