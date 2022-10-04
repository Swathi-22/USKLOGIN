# Generated by Django 4.1.1 on 2022-10-04 08:46

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_tools'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingTips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Forms/', verbose_name='Image')),
                ('ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20, verbose_name='Image PPOI')),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Marketing Tips',
            },
        ),
    ]
