# Generated by Django 5.0 on 2023-12-16 23:48

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_reserva_foto_remove_reserva_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='valor_final',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10),
        ),
    ]
