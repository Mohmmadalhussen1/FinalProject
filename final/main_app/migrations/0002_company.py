# Generated by Django 4.1.13 on 2024-10-30 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2048)),
                ('description', models.TextField()),
                ('contact_number', models.CharField(max_length=2048)),
            ],
        ),
    ]