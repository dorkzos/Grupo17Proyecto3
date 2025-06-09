#sofiii     ---------
from django.shortcuts import render, redirect
from .forms import LibroForm 
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm
from .models import Libro, CarritoUser, CarritoActual
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
    from tiendalibros.models import Historial
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
    from tiendalibros.models import Historial
    historial = Historial.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'historial_compras.html', {'historial': historial})


from .models import Libro

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
