# Generated by Django 4.1.1 on 2022-10-20 10:52

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_userregistration_is_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='profile_image',
            field=versatileimagefield.fields.VersatileImageField(default='Profile/deafult-01.jpg', null=True, upload_to='Profile'),
        ),
    ]