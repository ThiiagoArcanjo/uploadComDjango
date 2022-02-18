from django.shortcuts import render
from . import models

def uploadArquivo(request):
    if request.method == "POST":
        tituloArquivo = request.POST["tituloArquivo"]
        uploadArquivo = request.FILES["uploadArquivo"]

        arquivo = models.Arquivo(
            titulo = tituloArquivo,
            uploadArquivo = uploadArquivo
        )
        arquivo.save()
    arquivos = models.Arquivo.objects.all()

    return render(request, "uploadcompython/upload-arquivo.html", context={"arquivos": arquivos})