# Generated by Django 2.2.4 on 2019-08-09 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pageserver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelform',
            name='lugar_origen',
            field=models.CharField(choices=[('Azu', 'Azuay'), ('Bol', 'Bolivar'), ('Cañ', 'Cañar'), ('Car', 'Carchi'), ('Chi', 'Chimborazo'), ('Cot', 'Cotopaxi'), ('El', 'El Oro'), ('Es', 'Esmeraldas'), ('Gal', 'Galápagos'), ('Gua', 'Guayas'), ('Imb', 'Imbabura'), ('Loj', 'Loja'), ('Los', 'Los Ríos'), ('Man', 'Manabí'), ('Mor', 'Morona Santiago'), ('Nap', 'Napo'), ('Ore', 'Orellana'), ('Pas', 'Pastaza'), ('Pic', 'Pichincha'), ('San', 'Santa Elena'), ('Sant', 'Santo Domingo de los Tsáchilas'), ('Suc', 'Sucumbios'), ('Tun', 'Tungurahua'), ('Zam', 'Zamora Chinchipe')], max_length=30),
        ),
    ]