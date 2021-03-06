# Generated by Django 3.0.8 on 2020-07-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='')),
                ('data_nascimento', models.DateField()),
                ('teste', models.CharField(choices=[('RT-PCR', 'RT-PCR'), ('Sorologia', 'Sorologia'), ('Teste Rápido - Antígenos', 'Teste Rápido - Antígenos'), ('Teste Rápido - Anticorpos', 'Teste Rápido - Anticorpos')], default='RT-PCR', max_length=30)),
                ('resultado', models.CharField(choices=[('Positivo', 'Positivo'), ('Negativo', 'Negativo')], default='Negativo', max_length=30)),
            ],
        ),
    ]
