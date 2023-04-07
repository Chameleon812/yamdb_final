# Generated by Django 3.2 on 2023-01-20 12:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20230119_1356'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Genre_Title',
            new_name='GenreTitle',
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(2023)], verbose_name='Год выпуска'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', 'User'), ('moderator', 'Modarator'), ('admin', 'Admin')], default='user', max_length=20, verbose_name='Пользовательская роль'),
        ),
    ]
