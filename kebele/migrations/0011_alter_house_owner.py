# Generated by Django 4.1.2 on 2023-02-10 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kebele', '0010_remove_idcard_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kebele.resident'),
        ),
    ]
