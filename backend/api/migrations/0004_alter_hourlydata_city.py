# Generated by Django 3.2.4 on 2021-06-06 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_hourlydata_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourlydata',
            name='city',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_city', to='api.city'),
        ),
    ]
