# Generated by Django 4.1.3 on 2023-02-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='accepted',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
