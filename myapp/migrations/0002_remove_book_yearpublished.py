# Generated by Django 3.2.8 on 2021-10-23 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='yearpublished',
        ),
    ]
