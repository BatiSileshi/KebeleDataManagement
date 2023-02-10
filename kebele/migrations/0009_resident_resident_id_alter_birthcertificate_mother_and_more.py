# Generated by Django 4.1.2 on 2023-02-10 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kebele', '0008_birthcertificate_birth_place_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='resident_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='birthcertificate',
            name='mother',
            field=models.ForeignKey(blank=True, limit_choices_to={'sex': 'Female'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mothers', to='kebele.resident'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='nationality',
            field=models.CharField(blank=True, default='Ethiopian', max_length=100, null=True),
        ),
    ]
