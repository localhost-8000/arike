# Generated by Django 3.2.12 on 2022-03-05 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treatments', '0006_auto_20220305_0056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientdisease',
            old_name='note',
            new_name='remarks',
        ),
        migrations.AddField(
            model_name='patientdisease',
            name='investigated_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patientdisease',
            name='treatment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='treatments.treatment'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DiseaseHistory',
        ),
    ]