# galeria/forms.py
from django import forms
from .models import Imagem

class ImagemForm(forms.ModelForm):
    class Meta:
        model = Imagem
        fields = '__all__'
        exclude = ['data_upload']
        

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dê um título para a imagem'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Descreva a imagem (opcional)'}),
            'imagem': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

        labels = {
            'titulo': 'Título da Imagem',
            'descricao': 'Descrição Detalhada',
            'imagem': 'Selecione o Arquivo',
        }

        help_texts = {
            'imagem': 'Formatos suportados: JPG, PNG, GIF, etc.',
        }