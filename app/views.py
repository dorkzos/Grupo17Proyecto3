#sofiii     ---------
from django.shortcuts import render, redirect
from .forms import LibroForm 
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from .models import Libro
from .forms import LibroForm
from django.shortcuts import get_object_or_404

def agregar_libro(request):
    from django.contrib import messages
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro agregado correctamente.')
            return redirect('catalogo_libros')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})
#sofiii  fin   ---------
# app/views.py


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('mi_cuenta')
    else:
        form = RegistroForm()
    return render(request, 'app/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('mi_cuenta')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def mi_cuenta_view(request):
    return render(request, 'app/mi_cuenta.html')

@login_required
def mis_pedidos_view(request):
    return render(request, 'app/mis_pedidos.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def catalogo_libros(request):
    libros = Libro.objects.all()
    return render(request, 'catalogo_libros.html', {'libros': libros})

def agregar_al_carrito(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    carrito = request.session.get('carrito', {})
    libro_id_str = str(libro_id)
    if libro_id_str in carrito:
        carrito[libro_id_str] += 1
    else:
        carrito[libro_id_str] = 1
    request.session['carrito'] = carrito
    return redirect('catalogo_libros')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    libros = Libro.objects.filter(pk__in=carrito.keys())
    carrito_items = []
    for libro in libros:
        cantidad = carrito.get(str(libro.pk), 0)
        precio = libro.precio if libro.precio is not None else 0
        total = precio * cantidad
        carrito_items.append({'libro': libro, 'cantidad': cantidad, 'total': total})
    return render(request, 'carrito.html', {'carrito_items': carrito_items})
