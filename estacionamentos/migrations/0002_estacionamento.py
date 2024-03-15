# Generated by Django 4.2.3 on 2024-03-15 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacionamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEmpresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacionamentos.empresa', verbose_name='Id da empresa proprietária do estacionamento')),
            ],
        ),
    ]
