# Generated by Django 4.0.4 on 2022-06-04 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('satandeer_app', '0002_tarjeta'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteTarjeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroTarjeta', models.IntegerField()),
                ('creditoMax', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='satandeer_app.cliente')),
                ('tarjeta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='satandeer_app.tarjeta')),
            ],
        ),
    ]
