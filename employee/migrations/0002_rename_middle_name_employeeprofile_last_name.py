# Generated by Django 4.1.2 on 2023-01-01 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeprofile',
            old_name='middle_name',
            new_name='last_name',
        ),
    ]
