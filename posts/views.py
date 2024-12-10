from django.shortcuts import render, redirect
from .models import Post, Autor, Categoria
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AutorForm()
    return render(request, 'posts/crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'posts/crear_categoria.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'posts/crear_post.html', {'form': form})

def buscar_posts(request):
    form = BusquedaForm(request.GET)
    posts = []
    if form.is_valid():
        titulo = form.cleaned_data.get('titulo')
        if titulo:
            posts = Post.objects.filter(titulo__icontains=titulo)
    return render(request, 'posts/buscar.html', {'form': form, 'posts': posts})