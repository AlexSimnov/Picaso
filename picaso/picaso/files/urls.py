from django.urls import path

from .views import FileListApiView, FileCreateApiView

urlpatterns = [
    path('', FileListApiView.as_view()),
    path('upload/', FileCreateApiView.as_view())
]
