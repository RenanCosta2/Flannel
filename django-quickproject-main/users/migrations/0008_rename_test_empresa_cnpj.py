# Generated by Django 4.2.3 on 2024-02-16 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_empresa_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='test',
            new_name='cnpj',
        ),
    ]
