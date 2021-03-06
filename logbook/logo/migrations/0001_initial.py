# Generated by Django 3.2.10 on 2021-12-22 09:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tailNumber', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Registration Number')),
                ('type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Aircraft Type')),
            ],
            options={
                'ordering': ['tailNumber'],
            },
        ),
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aptIcao', models.CharField(blank=True, max_length=4, unique=True, verbose_name='ICAO Code')),
                ('aptIata', models.CharField(blank=True, max_length=3, unique=True, verbose_name='IATA Code')),
                ('aptCity', models.CharField(blank=True, max_length=20, verbose_name="City's Name")),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name="Pilot's Name")),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flightDate', models.DateField(verbose_name='Date of the Flight (DdMmYy) ')),
                ('flightNum', models.CharField(blank=True, max_length=10, verbose_name='Flight Number')),
                ('depTime', models.TimeField(blank=True, null=True, verbose_name='Departure Time (HhMm) ')),
                ('arrTime', models.TimeField(blank=True, null=True, verbose_name='Arrival Time (HhMm) ')),
                ('pilotRole', models.CharField(blank=True, choices=[('P1', 'Pilot in Command'), ('P2', 'First Officer')], max_length=2, null=True, verbose_name='Select Pilot Role')),
                ('nightTime', models.DurationField(blank=True, default=datetime.timedelta(0), null=True, verbose_name='Night')),
                ('dayTime', models.DurationField(blank=True, default=datetime.timedelta(0), null=True, verbose_name='Day')),
                ('sectorTime', models.DurationField(blank=True, default=datetime.timedelta(0), null=True, verbose_name='Block')),
                ('p1Time', models.DurationField(blank=True, default=datetime.timedelta(0), null=True, verbose_name='PIC')),
                ('p2Time', models.DurationField(blank=True, default=datetime.timedelta(0), null=True, verbose_name='P2')),
                ('arrApt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='arrival', to='logo.airport', verbose_name='Select Arrival Airport')),
                ('coPilot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='logo.people', verbose_name='Select First Officer')),
                ('depApt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='departure', to='logo.airport', verbose_name='Select Departure Airport')),
                ('tailNum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='logo.aircraft', verbose_name='Select Aircraft')),
            ],
            options={
                'ordering': ['-flightDate', '-depTime'],
            },
        ),
    ]
