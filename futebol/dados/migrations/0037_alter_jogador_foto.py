# Generated by Django 4.2.1 on 2023-07-29 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0036_alter_jogador_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='jogador_fotos/'),
        ),
    ]
