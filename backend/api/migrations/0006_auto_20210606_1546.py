# Generated by Django 3.2.4 on 2021-06-06 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210606_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='hourlydata',
            name='clouds',
            field=models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='hourlydata',
            name='dew_point',
            field=models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='hourlydata',
            name='dt',
            field=models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='hourlydata',
            name='feels_like',
            field=models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='hourlydata',
            name='humidity',
            field=models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='hourlydata',
            name='pressure',
            field=models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='hourlydata',
            name='temp',
            field=models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='hourlydata',
            name='uvi',
            field=models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='hourlydata',
            name='visibility',
            field=models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='hourlydata',
            name='weather',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='hourlydata',
            name='wind_deg',
            field=models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='hourlydata',
            name='wind_gust',
            field=models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=22, null=True),
        ),
        migrations.AddField(
            model_name='hourlydata',
            name='wind_speed',
            field=models.DecimalField(blank=True, decimal_places=16, default=0, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='hourlydata',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='api_city', to='api.city'),
        ),
    ]
