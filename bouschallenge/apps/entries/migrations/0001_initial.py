# Generated by Django 4.2.2 on 2023-06-18 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=150, verbose_name='Cliente')),
                ('contract_number', models.CharField(max_length=10, verbose_name='Número de contrato')),
                ('purchase_date', models.DateField(verbose_name='Fecha de compra')),
                ('city', models.CharField(max_length=255, verbose_name='Ciudad')),
                ('business', models.CharField(max_length=255, verbose_name='Empresa')),
                ('debt', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor adeudado')),
                ('file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='entry', to='files.uploadedfiles', verbose_name='Archivo')),
            ],
            options={
                'db_table': 'file_entries',
            },
        ),
    ]
