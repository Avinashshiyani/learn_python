# Generated by Django 5.1.2 on 2024-12-19 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='dep',
            new_name='department',
        ),
    ]
