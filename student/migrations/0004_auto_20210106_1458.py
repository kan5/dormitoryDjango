# Generated by Django 3.1.3 on 2021-01-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20210106_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.CharField(max_length=50),
        ),
    ]
