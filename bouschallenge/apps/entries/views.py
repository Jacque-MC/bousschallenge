from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from drf_spectacular.utils import extend_schema

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
    
    @extend_schema(
            request=FileEntriesDetailsSerializer,
            responses={200: FileEntriesDetailsSerializer},
            description=('Return all data entries associated '
                         'to an uploaded file id')
    )
    def retrieve(self, request, pk):
        obj = self.get_object(pk)
        serializer = FileEntriesDetailsSerializer(instance=obj)

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
            request=FileEntryListSerializer,
            responses={200: FileEntryListSerializer},
            description=('Return a list of all the entries '
                         'uploaded to the DB.')
    )
    def list(self, request):
        entries_list = self.get_queryset()
        page = self.paginate_queryset(entries_list)
        if page is not None:
            serializer = FileEntryListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = FileEntryListSerializer(entries_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
