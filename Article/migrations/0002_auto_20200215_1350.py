# Generated by Django 2.2.1 on 2020-02-15 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='article',
            table='Article',
        ),
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
        migrations.AlterModelTable(
            name='type',
            table='type',
        ),
    ]
