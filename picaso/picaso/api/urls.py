from django.urls import path, include

urlpatterns = [
    path('files/', include('files.urls')),
]
