# Generated by Django 4.2.3 on 2024-03-20 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_gerentegeral_gerentelocal_delete_userprofileexample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gerentegeral',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='gerentelocal',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='E-mail'),
        ),
    ]
