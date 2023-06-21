from django.db import models


class UploadedFiles(models.Model):
    filename = models.CharField(max_length=255, 
                                verbose_name='Nombre del archivo')
    upload_date = models.DateTimeField(auto_now_add=True, 
                                       verbose_name='Fecha de carga')

    class Meta:
        db_table = 'uploaded_files'
