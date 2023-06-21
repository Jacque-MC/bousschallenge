from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.entries.models import FileEntry
from apps.entries.serializers import FileEntryListSerializer
from apps.files.models import UploadedFiles
from apps.files.serializers import FileEntriesDetailsSerializer


class FileEntryView(GenericViewSet):
    def get_object(self, pk):
        obj = get_object_or_404(UploadedFiles, pk=pk)

        return obj
    
    def get_queryset(self):
        return FileEntry.objects.all()
    
    def retrieve(self, request, pk):
        """
        Returns a queryset of entries associated to a file id
        """
        obj = self.get_object(pk)
        serializer = FileEntriesDetailsSerializer(instance=obj)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def list(self, request):
        pagination_class = (PageNumberPagination,)
        entries_list = self.get_queryset()
        serializer = FileEntryListSerializer(entries_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
