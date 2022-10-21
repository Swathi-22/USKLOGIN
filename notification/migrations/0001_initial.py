# Generated by Django 4.1.1 on 2022-10-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('broadcast_on', models.DateTimeField()),
                ('send', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-broadcast_on'],
            },
        ),
    ]
