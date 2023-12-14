from django.forms import ModelForm
from django import forms
from .models import Post



class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'descripcion','urlimg']
        labels = {
            'titulo': 'Titulo',
            'subtitulo': 'Sub titulo',
            'descripcion':'Descripción',
            'urlimg':'Imagen',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese un titulo'}),
            'subtitulo': forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Ingrese un sub titulo'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control mb-3','placeholder':'Ingrese una descripción'}),
            'urlimg': forms.FileInput(attrs={'class':'form-control mb-3'}),

        }