from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    uploaded_at = serializers.DateTimeField(read_only=True)
    processed = serializers.BooleanField(read_only=True)

    class Meta:
        model = File
        fields = ('file',
                  'uploaded_at',
                  'processed')
