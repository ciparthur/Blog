from django import forms

from .models import BlogPost

class NovoPost(forms.ModelForm):
    def clean_data_titulo(self):
        data = self.cleaned_data['titulo']
        
        return data
    
    def clean_data_texto(self):
        data = self.cleaned_data['texto']
        
        return data
    
    class Meta:
        model = BlogPost
        fields = ['titulo', 'texto']


class EditarPost(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['titulo', 'texto']

        def clean_data_titulo(self):
            data = self.cleaned_data['titulo']

            return data

        def clean_data_texto(self):
            data = self.cleaned_data['texto']

            return data
