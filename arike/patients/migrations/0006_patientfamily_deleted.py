# Generated by Django 3.2.12 on 2022-03-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20220303_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientfamily',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]