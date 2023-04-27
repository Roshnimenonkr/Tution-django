# Generated by Django 4.1.6 on 2023-03-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('Standard', models.CharField(max_length=15)),
                ('Phone', models.IntegerField()),
                ('Password', models.CharField(max_length=15)),
                ('ConPassword', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, verbose_name='Name')),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='Tutor', verbose_name='Image')),
                ('Subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('Qualification', models.CharField(max_length=30, verbose_name='Qualification')),
                ('Experience', models.IntegerField(verbose_name='Experience')),
                ('Email', models.EmailField(max_length=254, verbose_name='Email')),
                ('Phone', models.IntegerField(verbose_name='Phone No')),
                ('Username', models.CharField(max_length=15, verbose_name='Set Username')),
                ('Password', models.CharField(max_length=15, verbose_name='Set Password')),
            ],
        ),
    ]