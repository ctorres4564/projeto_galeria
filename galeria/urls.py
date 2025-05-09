# galeria/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_imagens, name='listar_imagens'),
    path('upload/', views.upload_imagem, name='upload_imagem'),
    # NOVA URL para editar uma imagem específica
    # <int:id_imagem> captura um inteiro da URL e passa como argumento 'id_imagem' para a view
    path('editar/<int:id_imagem>/', views.editar_imagem, name='editar_imagem'),
    # NOVA URL para excluir uma imagem específica
    path('excluir/<int:id_imagem>/', views.excluir_imagem, name='excluir_imagem'),
]