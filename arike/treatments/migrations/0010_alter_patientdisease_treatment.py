# Generated by Django 3.2.12 on 2022-03-05 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0009_alter_patientdisease_treatment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdisease',
            name='treatment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='treatments.treatment'),
        ),
    ]