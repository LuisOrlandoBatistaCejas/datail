# Generated by Django 2.1.7 on 2019-02-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comprobante_detalles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprobantedetalles',
            name='id',
            field=models.TextField(auto_created=True, db_column='Id', primary_key=True, serialize=False, unique=True),
        ),
    ]