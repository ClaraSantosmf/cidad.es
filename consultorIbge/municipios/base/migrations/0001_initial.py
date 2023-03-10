# Generated by Django 4.0.5 on 2023-02-02 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metadados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regiao', models.CharField(blank=True, max_length=25)),
                ('pib', models.FloatField()),
                ('idh', models.FloatField()),
                ('extensao_territorial', models.FloatField()),
                ('densidade_demografica', models.FloatField()),
                ('populacao_estimada', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UF',
            fields=[
                ('id_ibge', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('sigla', models.TextField()),
                ('metadados', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.metadados')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id_ibge', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.TextField()),
                ('uf_sigla', models.TextField()),
                ('metadados', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.metadados')),
                ('uf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.uf')),
            ],
        ),
    ]
