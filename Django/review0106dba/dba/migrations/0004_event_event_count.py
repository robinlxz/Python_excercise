# Generated by Django 2.2.5 on 2020-01-09 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dba', '0003_duty_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_count',
            field=models.IntegerField(default=0),
        ),
    ]
