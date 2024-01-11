# Generated by Django 5.0 on 2023-12-17 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_remove_reserva_foto_evento_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to='usuarios.cliente'),
        ),
    ]
