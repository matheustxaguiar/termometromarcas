# Generated by Django 4.1.2 on 2022-11-03 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filtro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Pesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(verbose_name='Data')),
                ('quantidade', models.IntegerField(verbose_name='Quantidade')),
                ('termo', models.CharField(max_length=30, verbose_name='Pesquisa')),
                ('filtro', models.ManyToManyField(to='termometromarcas.filtro')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.CharField(max_length=280, verbose_name='Conteudo')),
                ('data', models.DateField(verbose_name='Data')),
                ('like', models.IntegerField(verbose_name='Like')),
                ('visualizacao', models.IntegerField(verbose_name='Visualizacao')),
                ('retweet', models.IntegerField(verbose_name='Retweet')),
                ('usuario', models.CharField(max_length=50, verbose_name='Usuario')),
                ('polaridade', models.IntegerField(verbose_name='Polaridade')),
                ('subjetividade', models.IntegerField(verbose_name='Subjetividade')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=30, verbose_name='Usuario')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('senha', models.CharField(max_length=30, verbose_name='Senha')),
                ('pesquisas', models.ManyToManyField(blank=True, to='termometromarcas.pesquisa')),
            ],
        ),
        migrations.CreateModel(
            name='Fisico',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='termometromarcas.usuario')),
                ('cpf', models.IntegerField(verbose_name='CPF')),
                ('status', models.CharField(choices=[('ativo', 'Ativo'), ('desativo', 'Desativo')], default='ativo', max_length=255)),
            ],
            bases=('termometromarcas.usuario',),
        ),
        migrations.CreateModel(
            name='Geografico',
            fields=[
                ('filtro_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='termometromarcas.filtro')),
                ('tipo', models.CharField(max_length=30, verbose_name='Tipo')),
                ('valor', models.CharField(max_length=30, verbose_name='Valor')),
            ],
            bases=('termometromarcas.filtro',),
        ),
        migrations.CreateModel(
            name='Juridico',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='termometromarcas.usuario')),
                ('cnpj', models.BigIntegerField(verbose_name='CPNJ')),
            ],
            bases=('termometromarcas.usuario',),
        ),
        migrations.CreateModel(
            name='Tempo',
            fields=[
                ('filtro_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='termometromarcas.filtro')),
                ('dataInicial', models.DateField(verbose_name='Data Inicial')),
                ('dataFinal', models.DateField(verbose_name='Data Final')),
            ],
            bases=('termometromarcas.filtro',),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='tweet',
            field=models.ManyToManyField(to='termometromarcas.tweet'),
        ),
    ]
