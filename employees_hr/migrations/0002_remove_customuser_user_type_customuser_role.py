# Generated by Django 5.0.6 on 2024-06-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees_hr', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_type',
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('superadmin', 'Super Admin'), ('admin', 'Admin'), ('staff', 'Staff'), ('user', 'User')], default='user', max_length=20),
        ),
    ]
