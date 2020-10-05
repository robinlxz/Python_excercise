# Generated by Django 2.2.5 on 2019-12-10 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regrets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='behavior',
            name='consequence',
            field=models.CharField(default='', help_text='What is the consequence?', max_length=400),
        ),
        migrations.AlterField(
            model_name='behavior',
            name='text',
            field=models.CharField(help_text='What have you done?', max_length=400),
        ),
    ]
