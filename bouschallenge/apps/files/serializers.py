from django.core.validators import FileExtensionValidator

import openpyxl
from rest_framework import serializers

from apps.entries.models import FileEntry
from apps.files.models import UploadedFiles

allowed_columns = [
    'Cliente',
    '# Contrato',
    'Fecha de Compra',
    'Ciudad',
    'Empresa',
    'Valor adeudado',
]


class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFiles
        fields = '__all__'


class UploadSerializer(serializers.ModelSerializer):
    xcelfile = serializers.FileField(
        validators=[FileExtensionValidator(
            allowed_extensions=['xlsx', 'xls', 'xlt']
        )]
    )

    class Meta:
        model = UploadedFiles
        fields = ('xcelfile', 'filename',)
        extra_kwargs = {
            'filename': {'required': False}
        }
    
    def create(self, validated_data):
        xcelfile = validated_data.get('xcelfile', '')
        file = UploadedFiles(filename=xcelfile.name)
        wb = openpyxl.load_workbook(xcelfile)
        sheet = wb.active
        columns = {}
        # get columns
        for row in sheet.iter_rows(min_col=1, max_col=7):
            for cell in row:
                if cell.value is None:
                    continue
                if cell.value in allowed_columns:
                    columns[cell.value] = cell
        r_col = list()
        r_col.append(columns[list(columns)[0]].col_idx)
        r_col.append(columns[list(columns)[-1]].col_idx)
    
        bulk_data = list()
        for row in sheet.iter_rows(min_col=r_col[0], 
                                   max_col=r_col[-1], 
                                   min_row=columns[list(columns)[0]].row+1):
            row_data = dict()
            for cell in row:
                if cell.value is None:
                    break
                row_data[list(columns)[cell.col_idx-2]] = cell.value
            if len(row_data) > 0:
                newrow=dict()
                for item in row_data:
                    newrow[dict(FileEntry.COL_NAMES)[item]] = row_data[item]
                    file.entries.add(newrow)
                    # bulk_data.append(newrow)
                    

        return False
