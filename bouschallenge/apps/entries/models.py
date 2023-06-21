from django.db import models
from apps.files.models import UploadedFiles


class FileEntry(models.Model):
    COL_NAMES = (
        ('Cliente', 'customer'),
        ('# Contrato', 'contract_number'),
        ('Ciudad', 'city'),
        ('Empresa', 'business'),
        ('Fecha de Compra', 'purchase_date'),
        ('Valor adeudado', 'debt'),
    )

    customer = models.CharField(max_length=150, 
                                verbose_name='Cliente')
    contract_number = models.CharField(max_length=10, 
                                       verbose_name='Número de contrato')
    purchase_date = models.DateTimeField(verbose_name='Fecha de compra')
    city = models.CharField(max_length=255, verbose_name='Ciudad')
    business = models.CharField(max_length=255, verbose_name='Empresa')
    debt = models.DecimalField(decimal_places=2, max_digits=8, 
                               verbose_name='Valor adeudado')
    file = models.ForeignKey(UploadedFiles, related_name='entries', 
                                on_delete=models.CASCADE, 
                                verbose_name='Archivo')

    class Meta:
        db_table = 'file_entries'
