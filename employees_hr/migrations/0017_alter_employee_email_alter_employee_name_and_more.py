# Generated by Django 5.0.6 on 2024-08-01 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_hr', '0016_employee_email_employee_salary_alter_employee_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
