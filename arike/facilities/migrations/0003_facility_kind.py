# Generated by Django 3.2.12 on 2022-02-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0002_auto_20220223_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='kind',
            field=models.CharField(choices=[(1, 'PHC'), (2, 'CHC')], default=1, max_length=100),
        ),
    ]
