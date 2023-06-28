from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet

from drf_spectacular.utils import extend_schema

from apps.files.models import UploadedFiles
from apps.files.serializers import (
    FileListSerializer, 
    UploadSerializer, 
    FileDetailsSerializer
)


class UploadedFilesViewset(GenericViewSet):
    def get_object(self, pk):
        obj = get_object_or_404(UploadedFiles, pk=pk)
        return obj
    
    def get_queryset(self):
        return UploadedFiles.objects.order_by('-upload_date')
    
    @extend_schema(
            request=FileListSerializer,
            responses={200: FileListSerializer},
            description=('Returns a list of uploaded files,'
                         ' ordered most recent to oldest.')
    )
    def list(self, request):
        files_list = self.get_queryset()
        page = self.paginate_queryset(files_list)
        if page is not None:
            serializer = FileListSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = FileListSerializer(files_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
            request=FileDetailsSerializer,
            responses={200: FileDetailsSerializer},
            description='Return data of a specific uploaded file'
    )
    def retrieve(self, request, pk):
        uploaded_file = self.get_object(pk)
        serializer = FileDetailsSerializer(instance=uploaded_file)            

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @extend_schema(
            request=FileDetailsSerializer,
            responses={200: FileDetailsSerializer},
            description='Return data of latest uploaded file',
    )
    def latest(self, request):
        uploaded_file = UploadedFiles.objects.order_by('-upload_date').first()
        serializer = FileDetailsSerializer(instance=uploaded_file)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpFileView(ViewSet):
    parser_classes = [MultiPartParser,]
    @extend_schema(
            request=UploadSerializer,
            responses={201: str},
            description=(
                'Upload an excel file and save'
                ' its data in the DB.'),
            methods=['POST']
    )
    def post(self, request, *args, **kwargs):
        response_data = {
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Incorrect data'
        }
        serializer = UploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data['status'] = status.HTTP_201_CREATED
            response_data['message'] = 'success'
        else:
            response_data['message'] = serializer.errors

        return Response(response_data)
