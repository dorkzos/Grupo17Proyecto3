#sofiii     ---------
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import LibroForm, ResenaForm
from .models import Libro, Historial, CarritoUser, CarritoActual, Resena
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseForbidden
from django.urls import reverse

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo_libros')
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})
#sofiii  fin   ---------
# app/views.py

@login_required
def ver_carrito(request):
    carrito_items = CarritoActual.objects.filter(usuario=request.user)
    items = []
    total_general = 0
    for item in carrito_items:
        precio = item.precio if item.precio is not None else 0
        total = precio * item.cantidad
        items.append({
            'titulo': item.titulo,
            'autor': item.autor,
            'categoria': item.categoria,
            'precio': precio,
            'cantidad': item.cantidad,
            'total': total,
            'fecha_publicacion': item.fecha_publicacion
        })
        total_general += total
    return render(request, 'carrito.html', {'carrito_items': items, 'total_general': total_general})

@login_required
def pagar(request):
    carrito_items = CarritoActual.objects.filter(usuario=request.user)
    for item in carrito_items:
        total = item.precio * item.cantidad
        Historial.objects.create(
            usuario=request.user,
            titulo=item.titulo,
            autor=item.autor,
            fecha_publicacion=item.fecha_publicacion,
            categoria=item.categoria,
            precio=item.precio,
            cantidad=item.cantidad,
            total=total,
            accion='Compra'
        )
    carrito_items.delete()
    return render(request, 'pagar.html')

@login_required
def historial_compras(request):
    historial = Historial.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'historial_compras.html', {'historial': historial})

def catalogo_libros(request):
    autor_filtrado = request.GET.get('autor')
    if autor_filtrado:
        libros = Libro.objects.filter(autor=autor_filtrado)
    else:
        libros = Libro.objects.all()
    autores = Libro.objects.values_list('autor', flat=True).distinct()
    return render(request, 'catalogo_libros.html', {
        'libros': libros,
        'autores': autores
    })

def agregar_resena(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.libro = libro
            resena.save()
            return redirect('catalogo_libros')
    else:
        form = ResenaForm()
    return render(request, 'agregar_resena.html', {'form': form, 'libro': libro})

def ver_resenas(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    resenas = Resena.objects.filter(libro=libro)
    return render(request, 'ver_resenas.html', {'libro': libro, 'resenas': resenas})

def inicio(request):
    if request.user.is_authenticated:
        return render(request, 'inicio_logueado.html', {'usuario': request.user})
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('inicio')
        else:
            form = AuthenticationForm()
        return render(request, 'inicio.html', {'form': form})

def registrarse(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
    else:
        form = UserCreationForm()
    return render(request, 'registrarse.html', {'form': form})

def usuario_logout(request):
    logout(request)
    return redirect('inicio')

@login_required
def agregar_al_carrito(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    carrito_item, created = CarritoActual.objects.get_or_create(
        usuario=request.user,
        titulo=libro.titulo,
        autor=libro.autor,
        fecha_publicacion=libro.fecha_publicacion,
        categoria=libro.categoria,
        precio=libro.precio
    )
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    return redirect('catalogo_libros')

def eliminar_libro(request, libro_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permisos para eliminar libros.")
    libro = get_object_or_404(Libro, id=libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect(reverse('catalogo_libros'))
    return render(request, 'eliminar_libro.html', {'libro': libro})
