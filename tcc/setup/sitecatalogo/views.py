from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CatalogoUsuario, CatalogoForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

def index(request):
    return render(request, 'index.html')

def categoria(request):
    return render(request, 'categoria.html')


def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
         
            usuario.password = form.cleaned_data['password']
            usuario.save()
            return redirect('index') 
    else:
        form = UsuarioForm()

    return render(request, 'registro.html', {'form': form})


@login_required
def catalogo_usuario(request):
    if request.method == 'POST':
        form = CatalogoUsuario(request.POST, request.FILES)
        if form.is_valid():
            catalogo = form.save(commit=False)
            catalogo.user = request.user
            catalogo.save()
            return redirect('index')
    else:
        form = CatalogoUsuario()
    return render(request, 'index.html', {'form': form})

def catalogo(request):
    if request.method == 'POST':
        form = CatalogoForm(request.POST, request.FILES)
        if form.is_valid():
            catalogo = form.save(commit=False)
            catalogo.user = request.user
            catalogo.save()
            return redirect('index')
    else:
        form = CatalogoForm()
    return render(request, 'catalogo_usuario.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
    

            if user:
                login(request, user)

                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


