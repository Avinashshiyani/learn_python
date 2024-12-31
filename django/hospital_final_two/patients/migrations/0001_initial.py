# Generated by Django 5.1.2 on 2024-12-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('age', models.IntegerField()),
                ('department', models.CharField(max_length=155)),
            ],
        ),
    ]
