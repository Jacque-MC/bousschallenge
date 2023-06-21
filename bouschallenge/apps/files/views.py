from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, GenericViewSet

from apps.files.models import UploadedFiles
from apps.files.serializers import FileListSerializer, UploadSerializer, FileDetailsSerializer


class UploadedFilesViewset(GenericViewSet):
    def get_object(self, pk):
        obj = get_object_or_404(UploadedFiles, pk=pk)

        return obj
    
    def get_queryset(self):
        return UploadedFiles.objects.order_by('-upload_date')
    
    def list(self, request):
        """
        Returns a list of uploaded files, ordered by latest to oldest
        """
        pagination_class = (PageNumberPagination,)
        files_list = self.get_queryset()
        serializer = FileListSerializer(files_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        uploaded_file = self.get_object(pk)
        serializer = FileDetailsSerializer(instance=uploaded_file)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpFileView(ViewSet):
    """
    View to upload and save excel file data
    """
    parser_classes = [MultiPartParser,]

    def post(self, request, *args, **kwargs):
        response_data = {
            'status': '400',
            'message': 'Incorrect data'
        }
        serializer = UploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response=serializer.save()

        if isinstance(response, UploadedFiles):
            response_data['status'] = status.HTTP_201_CREATED
            response_data['message'] = 'success'

        return Response(response_data)
