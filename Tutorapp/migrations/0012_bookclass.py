# Generated by Django 4.1.6 on 2023-04-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorapp', '0011_alter_requestdemo_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=15)),
                ('standard', models.CharField(max_length=10)),
                ('tutor', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('total_time', models.IntegerField()),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
