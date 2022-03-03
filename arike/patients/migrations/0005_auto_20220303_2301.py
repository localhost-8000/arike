# Generated by Django 3.2.12 on 2022-03-03 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_alter_patientfamily_relation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientfamily',
            name='education',
            field=models.CharField(choices=[('1', '10th Passed'), ('2', '12th Passed'), ('3', 'Graduation'), ('4', 'Post Graduation'), ('5', 'PhD'), ('6', 'Illiterate'), ('7', 'Others')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='patientfamily',
            name='relation',
            field=models.CharField(choices=[('1', 'Father'), ('2', 'Mother'), ('3', 'Son'), ('4', 'Sister'), ('5', 'GrandFather'), ('6', 'GrandMother'), ('7', 'Uncle'), ('8', 'Aunt'), ('9', 'Others')], default='1', max_length=50),
        ),
    ]