# Generated by Django 3.1.3 on 2021-01-06 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210105_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city_of_registration',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Cities',
        ),
        migrations.DeleteModel(
            name='Groups',
        ),
    ]