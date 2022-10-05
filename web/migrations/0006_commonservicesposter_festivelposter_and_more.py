# Generated by Django 4.1.1 on 2022-10-03 03:53

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_alter_userregistration_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonServicesPoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='CommonServices/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'Common Services Poster',
            },
        ),
        migrations.CreateModel(
            name='FestivelPoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='FestivelPoster/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'Festivel Poster',
            },
        ),
        migrations.CreateModel(
            name='ProfessionalPoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='ProfessionalPoster/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
            ],
            options={
                'verbose_name_plural': 'Professional Poster',
            },
        ),
    ]