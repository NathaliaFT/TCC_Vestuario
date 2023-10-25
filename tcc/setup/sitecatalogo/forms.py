from django import forms
from .models import Catalogo
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm

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


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


TEXT_WIDGETS = {
    'name': forms.TextInput,
    'subtitle': forms.TextInput,
    'description': forms.Textarea,
    'date_photography': forms.DateInput,
    'path': forms.ClearableFileInput
}

SELECT_WIDGETS = {
    'user': forms.Select,
    'category': forms.Select
}

COMMON_ATTRS = {
    'class': 'form-control',
    
}

class CatalogoUsuario(forms.ModelForm):
    class Meta:
        model = Catalogo
        fields = ['name', 'subtitle', 'user', 'category', 'description', 'date_photography', 'path']
        labels = {
            'name': "Nome:",
            'subtitle': "Subtitulo:",
            'user': "Usuário:",
            'category': "Categoria:",
            'date_photography': "Data da imagem:",
            'description': "Descrição:"
        }
        widgets = {
            field: widget(attrs=COMMON_ATTRS) for field, widget in TEXT_WIDGETS.items()
        }
        widgets.update({
            field: widget(attrs={**COMMON_ATTRS, 'class': 'form-select'}) for field, widget in SELECT_WIDGETS.items()
        })



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))