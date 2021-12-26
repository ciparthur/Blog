from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import NovoPost, EditarPost

def index(request):
    posts = BlogPost.objects.all().order_by('-data_add')
    
    contexto = {'posts': posts}
    
    return render(request, 'blogs/index.html', contexto)

def novo_post(request):
    post = BlogPost.objects.all()

    if request.method == 'POST':
        formulario = NovoPost(request.POST)

        if formulario.is_valid():
            post = BlogPost.objects.create()

            post.titulo = formulario.cleaned_data['titulo']
            post.texto = formulario.cleaned_data['texto']

            post.save()
            
            return HttpResponseRedirect(reverse('index'))
    else:
        formulario = NovoPost()

    contexto = {'formulario': formulario, 'post': post}

    return render(request, 'blogs/novo_post.html', contexto)

def editar_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    
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
