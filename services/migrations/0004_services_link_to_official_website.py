# Generated by Django 4.1.1 on 2022-10-01 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_services_about_service_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='link_to_official_website',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
