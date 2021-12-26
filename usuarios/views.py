from django.shortcuts import render
from django.contrib.auth import logout, login
from django.contrib.auth.forms import authenticate, UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def sair(request):
    logout(request)
    
    return HttpResponseRedirect(reverse('index'))

def cadastro(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():
            novo_usuario = formulario.save()

            usuario_autenticacao = authenticate(username=novo_usuario.username, password=request.POST['password1'])

            login(request, usuario_autenticacao)

            return HttpResponseRedirect(reverse('index'))
    else:
        formulario = UserCreationForm()
    
    contexto = {'formulario': formulario}
    
    return render(request, 'registration/cadastro.html', contexto)
