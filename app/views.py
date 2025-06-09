

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