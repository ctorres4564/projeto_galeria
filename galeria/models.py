# galeria/models.py
from django.db import models
from django.utils import timezone # Para registrar a data/hora

class Imagem(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição")
    imagem = models.ImageField(upload_to='imagens_galeria/', verbose_name="Arquivo da Imagem")
    data_upload = models.DateTimeField(default=timezone.now, verbose_name="Data de Upload")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Imagem"
        verbose_name_plural = "Imagens"
        ordering = ['-data_upload'] # Ordenar da mais recente para a mais antiga
