# Generated by Django 4.1.3 on 2023-02-04 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('admin', 'admin'), ('oprator', 'oprator')], max_length=10)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
