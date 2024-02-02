from rest_framework import generics, status
from rest_framework.response import Response

from .models import File

from .serializers import FileSerializer

from .tasks import upload_file


class FileListApiView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FileCreateApiView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request):
        serilizer = self.get_serializer(data=request.data)
        if serilizer.is_valid():
            file = serilizer.save()
            upload_file.delay(file.id)
            return Response(serilizer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serilizer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
