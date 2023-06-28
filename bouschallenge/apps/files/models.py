from django.db import models
from django.db.models import Sum, Func


class UploadedFiles(models.Model):
    filename = models.CharField(max_length=255, 
                                verbose_name='Nombre del archivo', unique=True)
    upload_date = models.DateTimeField(auto_now_add=True, 
                                       verbose_name='Fecha de carga')

    class Meta:
        db_table = 'uploaded_files'

    @property
    def get_grand_total(self):
        return self.entries.aggregate(total_debt=Sum('debt'))['total_debt']

    @property
    def grand_debt_by_city(self):
        return self.entries.values('city')\
            .annotate(
                total=((Sum('debt') / self.get_grand_total) * 100)
            )

    @property
    def grand_debt_by_business(self):
        return self.entries\
            .values('business')\
                .annotate(
                   total=( (Sum('debt') / self.get_grand_total) * 100 )
                )
