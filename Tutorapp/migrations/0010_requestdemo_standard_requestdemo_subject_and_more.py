# Generated by Django 4.1.6 on 2023-04-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorapp', '0009_requestdemo_date_requestdemo_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestdemo',
            name='standard',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='requestdemo',
            name='subject',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='requestdemo',
            name='student',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='requestdemo',
            name='tutor',
            field=models.CharField(max_length=15),
        ),
    ]
