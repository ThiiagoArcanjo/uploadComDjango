from datetime import timezone
from distutils.command.upload import upload
from django.db import models


class Arquivo(models.Model):
    titulo = models.CharField(max_length=200)
    uploadArquivo = models.FileField(upload_to="upload/")
    dataDoUpLoad = models.DateTimeField(auto_now=True)