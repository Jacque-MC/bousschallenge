from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.entries.models import FileEntry
from apps.entries.serializers import FileEntryListSerializer


class FileEntryView(ViewSet):
    def list(self, request):
        entries_list = FileEntry.objects.all()
        serializer = FileEntryListSerializer(entries_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
