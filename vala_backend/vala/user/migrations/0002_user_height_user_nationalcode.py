# Generated by Django 4.1.3 on 2023-02-15 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='nationalcode',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
