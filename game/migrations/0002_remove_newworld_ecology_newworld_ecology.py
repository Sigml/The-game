# Generated by Django 5.0.7 on 2024-11-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0015_alter_countryresource_resource'),
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newworld',
            name='ecology',
        ),
        migrations.AddField(
            model_name='newworld',
            name='ecology',
            field=models.ManyToManyField(blank=True, related_name='worlds', to='admin_panel.ecology'),
        ),
    ]
