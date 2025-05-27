from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Imagem
from .forms import ImagemForm
import os
from django.conf import settings

class ImagemModelTest(TestCase):
    def setUp(self):
        # Criar uma imagem de teste
        self.imagem = Imagem.objects.create(
            titulo="Teste Imagem",
            descricao="Descrição de teste",
            imagem=SimpleUploadedFile(
                name='test_image.jpg',
                content=b'',
                content_type='image/jpeg'
            )
        )

    def test_imagem_creation(self):
        self.assertTrue(isinstance(self.imagem, Imagem))
        self.assertEqual(self.imagem.__str__(), "Teste Imagem")

    def test_imagem_ordering(self):
        # Criar outra imagem para testar ordenação
        nova_imagem = Imagem.objects.create(
            titulo="Nova Imagem",
            descricao="Nova descrição",
            imagem=SimpleUploadedFile(
                name='test_image2.jpg',
                content=b'',
                content_type='image/jpeg'
            )
        )
        imagens = Imagem.objects.all()
        self.assertEqual(imagens[0], nova_imagem)  # A mais recente deve vir primeiro

class ImagemViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.listar_url = reverse('listar_imagens')
        self.upload_url = reverse('upload_imagem')
        
        # Criar uma imagem de teste
        self.imagem = Imagem.objects.create(
            titulo="Teste Imagem",
            descricao="Descrição de teste",
            imagem=SimpleUploadedFile(
                name='test_image.jpg',
                content=b'',
                content_type='image/jpeg'
            )
        )

    def test_listar_imagens_view(self):
        response = self.client.get(self.listar_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'galeria/listar_imagens.html')
        self.assertContains(response, "Teste Imagem")

    def test_upload_imagem_view_get(self):
        response = self.client.get(self.upload_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'galeria/upload_imagem.html')

    def test_upload_imagem_view_post(self):
        # Caminho para a imagem de teste
        # settings.BASE_DIR aponta para a raiz do seu projeto Django
        image_path = os.path.join(settings.BASE_DIR, 'galeria', 'test_assets', 'test_image.png')

        try:
            with open(image_path, 'rb') as f:
                image_content = f.read()
        except FileNotFoundError:
            self.fail(f"Arquivo de imagem de teste não encontrado em: {image_path}. "
                      "Certifique-se de que 'galeria/test_assets/test_image.png' existe.")

        imagem_teste = SimpleUploadedFile(
            name='test_image.png', # O nome que o arquivo terá no upload
            content=image_content,  # O conteúdo binário real do arquivo
            content_type='image/png'
        )
        
        data = {
            'titulo': 'Nova Imagem',
            'descricao': 'Nova descrição',
            'imagem': imagem_teste
        }
        response = self.client.post(self.upload_url, data)
        
        if response.status_code != 302:
            if response.context and 'form' in response.context:
                print("Form errors:", response.context['form'].errors)
            else:
                print("Form not in context or context is None. Status code:", response.status_code)

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Imagem.objects.filter(titulo='Nova Imagem').exists())

    def test_editar_imagem_view(self):
        edit_url = reverse('editar_imagem', args=[self.imagem.id])
        response = self.client.get(edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'galeria/editar_imagem.html')

    def test_excluir_imagem_view(self):
        delete_url = reverse('excluir_imagem', args=[self.imagem.id])
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)  # Redirecionamento após exclusão
        self.assertFalse(Imagem.objects.filter(id=self.imagem.id).exists())

class ImagemFormTest(TestCase):
    def test_imagem_form_valid(self):
        form_data = {
            'titulo': 'Teste Form',
            'descricao': 'Descrição do formulário'
        }
        form = ImagemForm(data=form_data)
        self.assertFalse(form.is_valid())  # Deve ser inválido sem imagem

    def test_imagem_form_invalid(self):
        form_data = {
            'titulo': '',  # Título vazio
            'descricao': 'Descrição do formulário'
        }
        form = ImagemForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('titulo', form.errors)
