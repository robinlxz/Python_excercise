# Generated by Django 2.2.5 on 2020-01-06 04:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duty_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200, unique=True)),
                ('event_times', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SubDuty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subduty_name', models.CharField(default='', max_length=200)),
                ('duty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dba.Duty')),
            ],
        ),
    ]