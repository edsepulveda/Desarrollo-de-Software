# Generated by Django 3.1.3 on 2021-05-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('1Web', '0002_auto_20210513_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tipo_categoria',
            field=models.IntegerField(choices=[[0, 'Guitarras'], [1, 'Bajos'], [2, 'Pianos'], [3, 'Baterias Acusticas'], [4, 'Bateria Electronica'], [5, 'Cabezales'], [6, 'Cajas'], [7, 'Audifonos'], [8, 'Monitores'], [9, 'Parlantes'], [10, 'Cables'], [11, 'Microfonos'], [12, 'Interfaces'], [13, 'Mixers']]),
        ),
    ]
