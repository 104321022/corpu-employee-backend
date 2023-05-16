# Generated by Django 4.2 on 2023-05-10 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("corpu_employee", "0006_alter_timetable_friday_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="timetable",
            name="course_code",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="corpu_employee.course",
            ),
        ),
        migrations.AlterField(
            model_name="timetable",
            name="user_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="corpu_employee.user",
            ),
        ),
    ]