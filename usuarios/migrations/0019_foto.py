# Generated by Django 5.0 on 2024-01-02 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0018_remove_evento_data_hora_fim_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='photos/')),
            ],
        ),
    ]
