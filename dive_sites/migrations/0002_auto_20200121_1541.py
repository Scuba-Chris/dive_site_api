# Generated by Django 3.0.2 on 2020-01-21 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dive_sites', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='divesite',
            old_name='authur',
            new_name='author',
        ),
    ]