# Generated by Django 4.1.6 on 2023-03-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorapp', '0003_rename_slug_tutor_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutor',
            name='Price',
            field=models.IntegerField(null=True, verbose_name='Charge per Hour'),
        ),
    ]
