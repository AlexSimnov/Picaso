from config.celery import app
from .models import File


@app.task
def upload_file(file_id):
    query = File.objects.get(id=file_id)
    query.processed = True
    query.save()
