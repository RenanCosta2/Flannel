# Generated by Django 4.2.3 on 2024-02-16 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idEmpresa', models.IntegerField()),
                ('idEndereco', models.IntegerField()),
                ('idGerente', models.IntegerField()),
                ('idfuncionario', models.IntegerField()),
            ],
        ),
    ]
