# Generated by Django 2.2.9 on 2020-02-03 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic_procedures', '0011_auto_20191127_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalregistrations',
            name='batch',
            field=models.IntegerField(default=2020),
        ),
        migrations.AlterField(
            model_name='initialregistrations',
            name='batch',
            field=models.IntegerField(default=2020),
        ),
        migrations.AlterField(
            model_name='register',
            name='year',
            field=models.IntegerField(default=2020),
        ),
    ]
