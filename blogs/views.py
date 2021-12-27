from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import NovoPost, EditarPost


def verificar_proprietario_pub(proprietario, usuario):
    """Verifica se o usuário é proprietário da conta"""
    if proprietario != usuario:
        raise Http404('Página não encontrada :(')


def post(request, post_pk):
    post = BlogPost.objects.get(pk=post_pk)
    
    contexto = {'post': post}
    
    return render(request, 'blogs/post.html', contexto)


def index(request):
    posts = BlogPost.objects.all().order_by('-data_add')

    contexto = {'posts': posts}

    return render(request, 'blogs/index.html', contexto)


@login_required
def novo_post(request):
    """Função view para adicionar novas publicações ao blog"""

    if request.method == 'POST':
        formulario = NovoPost(request.POST)

        if formulario.is_valid():
            post = formulario.save(commit=False)

            post.proprietario = request.user

            post.save()

            return HttpResponseRedirect(reverse('index'))
    else:
        formulario = NovoPost()

    contexto = {'formulario': formulario}

    return render(request, 'blogs/novo_post.html', contexto)


@login_required
def editar_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)

    verificar_proprietario_pub(post.proprietario, request.user)

    if request.method == 'POST':
        formulario = EditarPost(data=request.POST, instance=post)

        if formulario.is_valid():
            post.titulo = formulario.cleaned_data['titulo']
            post.texto = formulario.cleaned_data['texto']

            post.save()

            return HttpResponseRedirect(reverse('index'))

    else:
        formulario = EditarPost(instance=post)

    contexto = {'formulario': formulario, 'post': post}

    return render(request, 'blogs/editar_post.html', contexto)
