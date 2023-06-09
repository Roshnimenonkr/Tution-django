# Generated by Django 4.1.6 on 2023-03-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tutorapp', '0004_tutor_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('Books', models.FileField(blank=True, null=True, upload_to='Library', verbose_name='Upload files')),
            ],
        ),
    ]
