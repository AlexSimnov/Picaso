import re
from os import path

PATTERN = r'\.(\w+)$'


def upload_to(instance, filename):
    file_dir = path.join('files',
                         re.search(PATTERN, filename).group(1), filename)
    return file_dir
