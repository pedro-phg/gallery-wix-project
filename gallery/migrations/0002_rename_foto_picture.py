# Generated by Django 4.1.7 on 2023-05-28 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Foto',
            new_name='Picture',
        ),
    ]