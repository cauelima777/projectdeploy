# Generated by Django 4.2.1 on 2023-07-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0016_alter_jogador_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='foto',
            field=models.ImageField(upload_to='media/jogador_fotos'),
        ),
    ]
