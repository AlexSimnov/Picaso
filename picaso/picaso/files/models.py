from django.db import models

from .upload import upload_to


class File(models.Model):
    file = models.FileField(upload_to=upload_to,
                            max_length=255)
    uploaded_at = models.DateTimeField(
        'время загрузки файла',
        auto_now_add=True,
    )
    processed = models.BooleanField(
        default=False
    )
