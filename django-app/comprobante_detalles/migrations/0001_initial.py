# Generated by Django 2.1.7 on 2019-02-23 11:40

from django.db import migrations, models
import sqlparse


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComprobanteDetalles',
            fields=[
                ('id', models.TextField(db_column='Id', primary_key=True, serialize=False, unique=True)),
                ('comprobante_ruc', models.TextField(db_column='comprobante_Ruc')),
                ('comprobante_numero', models.TextField(db_column='comprobante_Numero')),
                ('codigo_principal', models.TextField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('cantidad', models.TextField()),
                ('precio', models.TextField(blank=True, null=True)),
                ('descuento', models.TextField(blank=True, null=True)),
                ('total', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comprobante_detalles',
            },
        ),
        migrations.RunSQL(
            sql=sqlparse.split('''
                    INSERT INTO comprobante_detalles VALUES ('664', '1792252903001', '002004000587976', 'PTQBPA', 'TRANSPORTE PASAJEROS TABABELA QUITO', '1.00000', '8.00000', '2.01000', '5.99000');
                    INSERT INTO comprobante_detalles VALUES ('665', '1792252903001', '002004000587976', 'TODTZ27', 'TRANSPORTE PASAJEROS SECTOR M', '1.00000', '3.00000', '0.00000', '3.00000');
                    INSERT INTO comprobante_detalles VALUES ('666', '1792252903001', '003001000586678', 'PQTBPA', 'TRANSPORTE PASAJEROS QUITO TABABELA', '1.00000', '8.00000', '0.01000', '7.99000');
                    INSERT INTO comprobante_detalles VALUES ('668', '2290324907001', '001001000001803', '274', 'PLOMO', '3.00000', '10.00000', '3.00000', '30.24000');
                    INSERT INTO comprobante_detalles VALUES ('669', '2290324907001', '001001000001803', '413', 'ZINC', '2.00000', '10.00000', '2.00000', '20.16000');
                    INSERT INTO comprobante_detalles VALUES ('670', '2290324907001', '001001000001803', '280', 'POTASIO', '3.00000', '10.00000', '3.00000', '30.24000');
                    INSERT INTO comprobante_detalles VALUES ('671', '2290324907001', '001001000001803', '95', 'CADMIO', '3.00000', '10.00000', '3.00000', '30.24000');
                    INSERT INTO comprobante_detalles VALUES ('672', '2290324907001', '001001000001803', '87', 'BIODEGRADABILIDAD', '2.00000', '50.00000', '10.00000', '100.80000');
                    INSERT INTO comprobante_detalles VALUES ('673', '2290324907001', '001001000001803', '147', 'DQO', '1.00000', '14.00000', '1.40000', '14.11000');
                    INSERT INTO comprobante_detalles VALUES ('674', '2290324907001', '001001000001803', '137', 'DBO5', '1.00000', '12.00000', '1.20000', '12.10000');
                    INSERT INTO comprobante_detalles VALUES ('675', '2290324907001', '001001000001803', '357', 'TENSOACTIVOS', '1.00000', '13.00000', '1.30000', '13.10000');
                    INSERT INTO comprobante_detalles VALUES ('680', '1792599512001', '001001000003704', '390', 'VITAMINA B1 (TIAMINA)', '1.00000', '30.00000', '0.00000', '33.60000');
                    INSERT INTO comprobante_detalles VALUES ('681', '1792599512001', '001001000003704', '394', 'VITAMINA B2 (RIBOFLAVINA)', '1.00000', '30.00000', '0.00000', '33.60000');
                    INSERT INTO comprobante_detalles VALUES ('699', '1791414713001', '001001000039698', 'TRANS-INC', 'SERVICIO DE TRANSPORTE', '1.00000', '90.00000', '0.00000', '90.00000');
                    INSERT INTO comprobante_detalles VALUES ('700', '1791414713001', '001001000039698', 'NE-40', 'TRATAMIENTO DE DESECHOS INDUSTRIALES', '3.00000', '1.80000', '0.00000', '6.05000');
                    INSERT INTO comprobante_detalles VALUES ('701', '1791414713001', '001001000039698', 'NE-29', 'TRATAMIENTO DE DESECHOS INDUSTRIALES', '42.00000', '0.90000', '0.00000', '42.34000');
                    INSERT INTO comprobante_detalles VALUES ('702', '1791414713001', '001001000039698', 'NE-23', 'TRATAMIENTO DE DESECHOS INDUSTRIALES', '20.50000', '0.90000', '0.00000', '20.66000');
                    INSERT INTO comprobante_detalles VALUES ('704', '1790016919001', '006111000362159', '786102290004', 'INDAVES HUEVO MEDIANO ESTUCHE', '1.00000', '1.94000', '0.00000', '1.94000');
                    INSERT INTO comprobante_detalles VALUES ('705', '1790016919001', '006111000362159', '786211311468', 'B VIDA INFUSIONES CEDRON', '2.00000', '0.80360', '0.00000', '1.80000');
                    INSERT INTO comprobante_detalles VALUES ('706', '1790016919001', '006111000362159', '770203210795', 'SELLO ROJO CAFE TOSTADO Y MOLIDO', '2.00000', '2.80360', '0.00000', '6.28000');
                    INSERT INTO comprobante_detalles VALUES ('707', '1790016919001', '006111000362159', '786100191104', 'SNOB MERMELADA PINA', '2.00000', '1.26790', '0.00000', '2.84000');
                    INSERT INTO comprobante_detalles VALUES ('708', '1790016919001', '006111000362159', '267666', 'MANZANA ROYAL GALA GRANEL.', '0.77500', '4.30970', '0.00000', '3.34000');
                    INSERT INTO comprobante_detalles VALUES ('709', '1790016919001', '006111000362159', '786100834066', 'LUNITAS GALL.ARTESANA', '1.00000', '1.59820', '0.00000', '1.79000');
                    INSERT INTO comprobante_detalles VALUES ('710', '1790016919001', '006111000362159', '786100834097', 'OREJAS HOJALDRE GALL. ART', '1.00000', '0.91070', '0.00000', '1.02000');
            ''')
        )
    ]
