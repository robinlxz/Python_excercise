# Generated by Django 2.2.5 on 2019-12-11 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event1210', '0002_question_question_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_odd',
            field=models.IntegerField(default=0),
        ),
    ]
