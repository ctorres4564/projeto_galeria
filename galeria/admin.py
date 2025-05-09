# galeria/admin.py
from django.contrib import admin
from .models import Imagem # Importa nosso modelo Imagem

@admin.register(Imagem) # Maneira moderna de registrar
class ImagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_upload', 'imagem') # Campos a mostrar na lista
    list_filter = ('data_upload',) # Filtros laterais
    search_fields = ('titulo', 'descricao') # Campos para busca

# Ou a forma mais simples (sem personalização da lista):
# admin.site.register(Imagem)
