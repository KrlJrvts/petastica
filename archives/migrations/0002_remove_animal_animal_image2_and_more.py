# Generated by Django 4.2 on 2023-05-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='animal_image2',
        ),
        migrations.AlterField(
            model_name='animal',
            name='animal_image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
