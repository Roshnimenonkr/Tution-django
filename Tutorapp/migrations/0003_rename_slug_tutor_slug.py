# Generated by Django 4.1.6 on 2023-03-26 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorapp', '0002_client_slug_tutor_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutor',
            old_name='Slug',
            new_name='slug',
        ),
    ]
