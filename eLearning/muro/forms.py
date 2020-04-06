from django import forms
from .models import *
import re


class AddNewAnuncio(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['titulo', 'texto', 'imagen']

    def clean_titulo(self):
        anuncio_name = self.cleaned_data['titulo']

        regexp = re.compile(r'[0-9a-zA-Z!.? ]')
        if not regexp.match(anuncio_name):
            raise forms.ValidationError("El título solo puede contener los siguientes caracteres: (a-z, A-Z, 0-9, !.?' ').")
        return anuncio_name


class AddNewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
