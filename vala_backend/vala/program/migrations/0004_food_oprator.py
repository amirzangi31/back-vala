# Generated by Django 4.1.3 on 2023-02-20 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_manager_image_alter_manager_types'),
        ('program', '0003_remove_diet_user_remove_sports_user_diet_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='oprator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manager.manager'),
            preserve_default=False,
        ),
    ]
