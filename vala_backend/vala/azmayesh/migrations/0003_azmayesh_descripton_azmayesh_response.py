# Generated by Django 4.1.3 on 2023-02-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azmayesh', '0002_azmayesh_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='azmayesh',
            name='descripton',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='azmayesh',
            name='response',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
