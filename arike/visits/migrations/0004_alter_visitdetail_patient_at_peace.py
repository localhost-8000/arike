# Generated by Django 3.2.12 on 2022-03-05 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0003_visitschedule_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitdetail',
            name='patient_at_peace',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False),
        ),
    ]