# Generated by Django 5.1.6 on 2025-03-05 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_video_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='slug',
        ),
    ]
