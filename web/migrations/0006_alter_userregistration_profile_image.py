# Generated by Django 4.1.1 on 2022-10-20 10:55

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_userregistration_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='profile_image',
            field=versatileimagefield.fields.VersatileImageField(default='deafult-01.jpg', null=True, upload_to='Profile'),
        ),
    ]
