# Generated by Django 3.1.2 on 2020-10-30 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(help_text='Código del producto', primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=200)),
                ('cant', models.IntegerField()),
            ],
        ),
    ]