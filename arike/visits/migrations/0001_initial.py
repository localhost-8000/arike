# Generated by Django 3.2.12 on 2022-03-03 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patients', '0003_auto_20220303_2033'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('duration', models.DurationField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nurse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
        ),
        migrations.CreateModel(
            name='VisitDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palliative_phase', models.CharField(max_length=50)),
                ('blood_pressure', models.CharField(max_length=50)),
                ('pulse', models.CharField(max_length=50)),
                ('general_random_blood_sugar', models.CharField(max_length=50)),
                ('personal_hygiene', models.CharField(max_length=50)),
                ('mouth_hygiene', models.CharField(max_length=50)),
                ('public_hygiene', models.CharField(max_length=50)),
                ('systemic_examination', models.CharField(max_length=50)),
                ('patient_at_peace', models.BooleanField(default=False)),
                ('pain', models.BooleanField(default=True)),
                ('symptoms', models.CharField(max_length=200)),
                ('note', models.CharField(max_length=400)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('visit_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visits.visitschedule')),
            ],
        ),
    ]
