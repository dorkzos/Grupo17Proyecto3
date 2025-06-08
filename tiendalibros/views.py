from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def inicio(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # Redirige a la misma vista para mostrar el mensaje de bienvenida
    else:
        form = AuthenticationForm()

    return render(request, 'inicio.html', {'form': form})

def usuario_logout(request):
    logout(request)
    return redirect('inicio')
