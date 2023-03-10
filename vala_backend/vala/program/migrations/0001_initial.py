# Generated by Django 4.1.3 on 2023-02-15 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_user_height_user_nationalcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('calories', models.IntegerField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.TimeField()),
                ('day', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Snack1', 'Snack1'), ('Lunch', 'Lunch'), ('Snack2', 'Snack2'), ('Dinner', 'Dinner')], max_length=20)),
                ('day', models.CharField(max_length=50)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='program.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
