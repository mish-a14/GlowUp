# Generated by Django 3.1.7 on 2021-04-07 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_hairdiary_supplements'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hairdiary',
            old_name='supplements',
            new_name='Supplements',
        ),
    ]
