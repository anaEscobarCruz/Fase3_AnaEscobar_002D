# Generated by Django 3.1.2 on 2020-11-30 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='orden',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='orderline',
            name='user',
        ),
        migrations.DeleteModel(
            name='Orden',
        ),
        migrations.DeleteModel(
            name='OrderLine',
        ),
    ]
