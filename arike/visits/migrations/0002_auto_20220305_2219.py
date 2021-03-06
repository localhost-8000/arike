# Generated by Django 3.2.12 on 2022-03-05 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitdetail',
            name='palliative_phase',
            field=models.CharField(choices=[('1', 'Stable'), ('2', 'Unstable'), ('3', 'Deteriorating'), ('4', 'Dying')], max_length=50),
        ),
        migrations.AlterField(
            model_name='visitdetail',
            name='systemic_examination',
            field=models.CharField(choices=[('1', 'Cardiovascular'), ('2', 'Central nervous system'), ('3', 'Gastrointestinal'), ('4', 'Genital-urinary'), ('5', 'Respiratory')], max_length=50),
        ),
    ]
