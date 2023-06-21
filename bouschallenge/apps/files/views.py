from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.files.models import UploadedFiles
from apps.files.serializers import FileListSerializer, UploadSerializer


class UploadedFilesViewset(ViewSet):
    def list(self, request):
        files_list = UploadedFiles.objects.order_by('upload_date')
        serializer = FileListSerializer(files_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# create view to upload and process excel files
class ReadFileView(ViewSet):
    parser_classes = [MultiPartParser,]

    def post(self, request, *args, **kwargs):
        serializer = UploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"status": "success"}, status.HTTP_201_CREATED)
