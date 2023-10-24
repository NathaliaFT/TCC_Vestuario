from django import forms
from .models import Catalogo

class CatalogoForm(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = [
            'name', 
            'subtitle', 
            'category', 
            'description', 
            'path', 
            'published', 
            'user'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=Catalogo.OPTIONS_CATEGORY, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'path': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }

