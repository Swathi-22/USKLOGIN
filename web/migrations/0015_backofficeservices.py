# Generated by Django 4.1.1 on 2022-10-04 11:07

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_agencyportal'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackOfficeServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Back_Office_Service/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Back Office Service',
            },
        ),
    ]
