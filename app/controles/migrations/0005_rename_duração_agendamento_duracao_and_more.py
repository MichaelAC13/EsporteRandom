# Generated by Django 4.1.6 on 2023-07-23 00:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controles', '0004_esporte_cor_esporte_icon_url_alter_agendamento_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agendamento',
            old_name='duração',
            new_name='duracao',
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 7, 23, 0, 45, 41, 790216, tzinfo=datetime.timezone.utc), null=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='esporte',
            name='tipo',
            field=models.CharField(blank=True, max_length=30, verbose_name='Tipo'),
        ),
    ]
