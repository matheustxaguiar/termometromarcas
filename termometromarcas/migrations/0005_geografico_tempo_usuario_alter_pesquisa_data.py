# Generated by Django 4.1.2 on 2022-10-18 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('termometromarcas', '0004_remove_pesquisa_tweet_pesquisa_tweet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geografico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=30, verbose_name='Tipo')),
                ('valor', models.CharField(max_length=30, verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Tempo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInicial', models.DateField(verbose_name='Data Inicial')),
                ('dataFinal', models.DateField(verbose_name='Data Final')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30, verbose_name='Usuario')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('senha', models.CharField(max_length=30, verbose_name='Senha')),
            ],
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='data',
            field=models.DateTimeField(verbose_name='Data'),
        ),
    ]
