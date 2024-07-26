# Generated by Django 5.0.6 on 2024-07-16 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_hr', '0011_rename_employee_name_attendance_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('return_date', models.DateField()),
                ('reason', models.TextField()),
            ],
        ),
    ]