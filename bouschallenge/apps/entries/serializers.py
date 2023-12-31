from decimal import Decimal
from rest_framework import serializers

from apps.entries.models import FileEntry


class FileEntryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileEntry
        fields = '__all__'


class CreateEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FileEntry
        fields = '__all__'

    def validate_debt(self, value):
        return Decimal(value)

    def validate_contract_number(self, value):
        return str(value)
    
    def validate_business(self, value):
        return str(value)
    
    def validate_city(self, value):
        return str(value)
    
    def validate_customer(self, value):
        return str(value)
