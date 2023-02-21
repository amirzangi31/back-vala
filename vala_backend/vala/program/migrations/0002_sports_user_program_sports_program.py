# Generated by Django 4.1.3 on 2023-02-15 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_manager_image_alter_manager_types'),
        ('user', '0002_user_height_user_nationalcode'),
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sports',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('types', models.CharField(choices=[('Food', 'Food'), ('Sport', 'Sport')], max_length=20)),
                ('oprator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.manager')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.AddField(
            model_name='sports',
            name='program',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='program.program'),
            preserve_default=False,
        ),
    ]