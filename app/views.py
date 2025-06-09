

#sofiii     ---------
from django.shortcuts import render, redirect
from .forms import LibroForm  # Asegúrate de tener este formulario creado

def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')  # cambia esto si tienes otra vista/listado
    else:
        form = LibroForm()
    return render(request, 'agregar_libro.html', {'form': form})
#sofiii  fin   ---------
# app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, LoginForm

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
