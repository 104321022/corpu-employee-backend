# Generated by Django 4.2.1 on 2023-05-08 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corpu_employee', '0003_user_userlocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('departmant_id', models.CharField(max_length=9, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=19)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corpu_employee.user')),
            ],
        ),
    ]
