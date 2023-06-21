from django.db import models


class UploadedFiles(models.Model):
    filename = models.CharField(max_length=255, 
                                verbose_name='Nombre del archivo', unique=True)
    upload_date = models.DateTimeField(auto_now_add=True, 
                                       verbose_name='Fecha de carga')

    class Meta:
        db_table = 'uploaded_files'

    @property
    def get_grand_total(self):
        return self.entries.aggregate(total_debt=models.Sum('debt'))

    @property
    def grand_debt_by_city(self):
        return self.entries.values('city')\
            .annotate(total=models.Sum('debt'))

    @property
    def grand_debt_by_business(self):
        return self.entries\
            .values('business')\
                .annotate(total=models.Sum('debt'))