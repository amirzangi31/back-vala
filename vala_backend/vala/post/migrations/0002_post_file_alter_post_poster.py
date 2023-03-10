# Generated by Django 4.1.3 on 2023-02-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(default=1, upload_to='home/post/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.ImageField(null=True, upload_to='', verbose_name='home/post/poster/'),
        ),
    ]
