# Generated by Django 3.2.12 on 2022-03-05 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visits', '0002_auto_20220305_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitschedule',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
