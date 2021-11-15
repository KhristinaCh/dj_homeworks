# Generated by Django 3.2.9 on 2021-11-07 19:01

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.IntegerField(primary_key=builtins.id, serialize=False)),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.TextField()),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField()),
                ('slug', models.TextField()),
            ],
        ),
    ]