# Generated by Django 5.0 on 2024-01-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0020_rename_title_foto_nome_remove_foto_image_foto_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='foto',
        ),
        migrations.AddField(
            model_name='cliente',
            name='cep',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
