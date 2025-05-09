# galeria/views.py
from django.shortcuts import render, redirect, get_object_or_404 # Adicione get_object_or_404
from .models import Imagem
from .forms import ImagemForm
from django.contrib import messages
import os # Para deletar o arquivo físico da imagem
from django.conf import settings # Para obter MEDIA_ROOT

def listar_imagens(request):  
    imagens = Imagem.objects.all()
    contexto = {'imagens': imagens}
    return render(request, 'galeria/listar_imagens.html', contexto)

def upload_imagem(request):
    if request.method == 'POST':
        form = ImagemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Imagem enviada com sucesso!')
            return redirect('listar_imagens')
        else:
            messages.error(request, 'Erro ao enviar a imagem. Verifique os dados.')
    else:
        form = ImagemForm()
    contexto = {'form': form}
    return render(request, 'galeria/upload_imagem.html', contexto)

# NOVA VIEW: Editar Imagem
def editar_imagem(request, id_imagem):
    # Busca a imagem específica pelo ID fornecido na URL, ou retorna erro 404 se não encontrada
    imagem_obj = get_object_or_404(Imagem, pk=id_imagem)

    if request.method == 'POST':
        # Cria um formulário com os dados enviados (request.POST),
        # os arquivos enviados (request.FILES),
        # e a instância da imagem que estamos editando (instance=imagem_obj)
        form = ImagemForm(request.POST, request.FILES, instance=imagem_obj)
        if form.is_valid():
            form.save() # Salva as alterações no objeto imagem_obj
            messages.success(request, f'Imagem "{imagem_obj.titulo}" atualizada com sucesso!')
            return redirect('listar_imagens')
        else:
            messages.error(request, 'Erro ao atualizar a imagem. Verifique os dados.')
    else:
        # Se for uma requisição GET, cria um formulário pré-preenchido
        # com os dados da imagem existente (instance=imagem_obj)
        form = ImagemForm(instance=imagem_obj)

    contexto = {
        'form': form,
        'imagem_obj': imagem_obj # Para exibir informações da imagem no template (ex: título atual)
    }
    return render(request, 'galeria/editar_imagem.html', contexto)

# NOVA VIEW: Excluir Imagem
def excluir_imagem(request, id_imagem):
    imagem_obj = get_object_or_404(Imagem, pk=id_imagem)

    if request.method == 'POST': # Se o formulário de confirmação foi enviado
        caminho_imagem_antiga = None
        if imagem_obj.imagem: # Verifica se existe um arquivo de imagem associado
            caminho_imagem_antiga = os.path.join(settings.MEDIA_ROOT, imagem_obj.imagem.name)

        titulo_imagem_excluida = imagem_obj.titulo
        imagem_obj.delete() # Exclui o objeto do banco de dados

        # Tenta excluir o arquivo físico da imagem do sistema de arquivos
        if caminho_imagem_antiga and os.path.exists(caminho_imagem_antiga):
            try:
                os.remove(caminho_imagem_antiga)
                messages.success(request, f'Imagem "{titulo_imagem_excluida}" e seu arquivo foram excluídos com sucesso!')
            except OSError as e:
                messages.warning(request, f'Imagem "{titulo_imagem_excluida}" excluída do banco, mas houve um erro ao remover o arquivo: {e}')
        else:
            messages.success(request, f'Imagem "{titulo_imagem_excluida}" (sem arquivo físico associado ou arquivo não encontrado) excluída do banco com sucesso!')

        return redirect('listar_imagens')

    # Se for GET, mostra a página de confirmação
    contexto = {'imagem_obj': imagem_obj}
    return render(request, 'galeria/confirmar_exclusao.html', contexto)