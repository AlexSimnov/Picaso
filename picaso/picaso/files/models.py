from django.db import models
from os import path
import re

PATTERN = r'\.(\w+)$'


def upload_to(instance, filename):
    file_dir = path.join('files',
                         re.search(PATTERN, filename).group(1), filename)
    return file_dir


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
