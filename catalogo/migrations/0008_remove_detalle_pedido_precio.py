# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-05 00:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_detalle_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalle_pedido',
            name='precio',
        ),
    ]
