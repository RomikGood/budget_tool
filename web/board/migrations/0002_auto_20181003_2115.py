# Generated by Django 2.1.2 on 2018-10-03 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='remaining_budget',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='budget',
            name='total_budget',
            field=models.FloatField(default=0.0),
        ),
    ]
