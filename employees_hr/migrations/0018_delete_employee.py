# Generated by Django 5.0.6 on 2024-08-01 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees_hr', '0017_alter_employee_email_alter_employee_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee',
        ),
    ]