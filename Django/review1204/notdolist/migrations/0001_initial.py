# Generated by Django 2.2.5 on 2019-12-04 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NotdoItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notdo_name', models.CharField(max_length=200, unique=True)),
                ('start_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
