# Generated by Django 4.0.3 on 2022-03-24 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memo',
            old_name='org',
            new_name='orgs',
        ),
        migrations.RenameField(
            model_name='memo',
            old_name='tag',
            new_name='tags',
        ),
    ]