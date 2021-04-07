# Generated by Django 3.1.7 on 2021-04-06 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210404_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skin_Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('skin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.skindiary')),
            ],
        ),
        migrations.CreateModel(
            name='Hair_Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=300)),
                ('hair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.hairdiary')),
            ],
        ),
    ]