# Generated by Django 5.0.7 on 2024-08-05 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='cauthor',
            new_name='author',
        ),
    ]
