# Generated by Django 4.0.5 on 2022-06-16 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='views',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
