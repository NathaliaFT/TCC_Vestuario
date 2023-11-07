from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CatalogoUsuario, CatalogoForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def index(request):
    return render(request, 'index.html')

def categoria(request):
    return render(request, 'categoria.html')

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            
            # Criptografa a senha antes de salvá-la
            usuario.password = make_password(form.cleaned_data['password'])
            usuario.save()

            # Autentica o usuário após o registro
            user = authenticate(username=usuario, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('dashboard')  # Redireciona superusuário para a página do painel de controle
                else:
                    return redirect('index')  # Redireciona outros usuários para a página inicial

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
            catalogo.save()
            return redirect('index')
    else:
        form = CatalogoForm()
    return render(request, 'catalogo_usuario.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('senha')

            user_temp = User.objects.filter(email=email).first()

            if user_temp is not None and user_temp.check_password(password):
                auth.login(request, user_temp)
                messages.success(request, 'Foi logado com sucesso!')
                return redirect('dashboard')

        messages.error(request, 'Erro ao efetuar login')
        return redirect('index')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})




