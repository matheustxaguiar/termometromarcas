# Generated by Django 4.1.2 on 2022-10-19 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('termometromarcas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='pesquisas',
            field=models.ManyToManyField(null=True, to='termometromarcas.pesquisa'),
        ),
    ]
