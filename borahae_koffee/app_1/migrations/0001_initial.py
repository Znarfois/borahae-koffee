# Generated by Django 4.0.2 on 2022-02-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=255)),
                ('LastName', models.CharField(max_length=255)),
                ('PhoneNumber', models.PositiveSmallIntegerField()),
                ('EMail', models.CharField(max_length=255)),
            ],
        ),
    ]
