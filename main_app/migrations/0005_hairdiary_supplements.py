# Generated by Django 3.1.7 on 2021-04-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210406_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='hairdiary',
            name='supplements',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
