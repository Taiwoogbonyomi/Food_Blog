# Generated by Django 4.2.16 on 2024-11-05 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodblog', '0002_comment_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='updated_at',
        ),
    ]
