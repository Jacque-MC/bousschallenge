from rest_framework import serializers

from apps.entries.models import FileEntry


class FileEntryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileEntry
        fields = '__all__'
