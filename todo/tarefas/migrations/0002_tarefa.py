# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2020-01-09 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('data_final', models.DateField(verbose_name='Data final')),
                ('prioridade', models.CharField(choices=[('B', 'Baixa'), ('M', 'Média'), ('A', 'Alta')], max_length=1, verbose_name='Prioridade')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tarefas.Categoria', verbose_name='Categoria')),
            ],
        ),
    ]
