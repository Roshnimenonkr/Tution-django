# Generated by Django 4.1.6 on 2023-04-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorapp', '0010_requestdemo_standard_requestdemo_subject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestdemo',
            name='subject',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
