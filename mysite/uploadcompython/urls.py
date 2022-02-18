from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "uploadComDjango"

urlpatterns = [
    path("", views.uploadArquivo, name ="uploadArquivo"),
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT,
    )